import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from typing import List, Annotated

import models


app = FastAPI()

origins = [
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecordBase(BaseModel):
    date: str
    name: str
    sets: int
    reps: int
    rating: str

class RecordModel(RecordBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

def fetch_db():
    db_connection = models.session_local()

    try:
        yield db_connection
    finally:
        db_connection.close()

db_dependency = Annotated[Session, Depends(fetch_db)]

models.base.metadata.create_all(bind=models.engine)

@app.post("/records/", response_model=RecordModel)
async def add_record(record: RecordBase, db: db_dependency):
    record = models.Records(**record.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@app.get("/records/", response_model=List[RecordModel])
async def read_records(db: db_dependency, skip: int = 0, limit: int = 100):
    records = db.query(models.Records).offset(skip).limit(limit).all()
    return records
