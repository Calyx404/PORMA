# Contributing Guidelines

Thank you for considering contributing to this project!
We welcome contributions of all kinds—bug reports, documentation, code, ideas.

---

## 🧾 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Commit Convention](#commit-convention)
- [Coding Standards](#coding-standards)
- [License](#license)

---

## 📜 Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.
Be respectful, inclusive, and constructive.

---

## 🛠 Getting Started

1. Fork the repository
2. Clone your forked repo:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Contribute

### 🐞 Report Bugs
- Use the issue template.
- Include reproducible steps, logs, and screenshots if applicable.

### ✍️ Suggest Features
- Describe the motivation and impact.
- Be clear about the proposed implementation.

### 🧑‍💻 Submit Code
- Open an issue first if it's a big feature.
- Submit pull requests from a new branch (`feature/your-feature-name`).
- Follow commit conventions (below).

---

## ✅ Pull Request Guidelines

- Describe **what** you changed and **why**.
- Reference related issues (`Fixes #123`).
- Include tests for new features or bug fixes.
- Run linting and tests locally before submitting

---

## 🔤 Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(scope): short description
```

Commit Type Reference
======================

| Type     | Description                                               | Example                                |
|----------|-----------------------------------------------------------|----------------------------------------|
| feat     | A new feature for the user or system                      | feat(cli): add project init option     |
| fix      | A bug fix                                                 | fix(env): correct dotenv parsing       |
| docs     | Documentation only changes                                | docs(readme): update usage section     |
| style    | Changes that do not affect the meaning (formatting, etc.)| style(api): apply code formatter       |
| refactor | Code change that neither fixes a bug nor adds a feature  | refactor(core): simplify logic         |
| perf     | A code change that improves performance                   | perf(query): optimize db lookups       |
| test     | Adding or fixing tests                                    | test(utils): add unit tests for calc   |
| chore    | Other changes (build process, CI configs)                 | chore(deps): upgrade flake8 version    |
| revert   | Revert a previous commit                                  | revert: revert feat(cli) commit        |
| ci       | Changes to CI/CD pipeline                                 | ci(github): add deploy job             |
| build    | Changes that affect the build system or dependencies      | build(requirements): add coverage.py   |

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as this project.
        