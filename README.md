# 🧰 The Manager — Centralized Python Virtual Environment Manager

A command-line tool that creates, stores, manages, and auto-activates Python virtual environments from a single global directory.

Instead of manually tracking environments across projects, all virtual environments are stored in one place and can be listed, renamed, deleted, or activated through an interactive menu.

Supports **Linux and Windows activation modes**.

---

## ✨ Features

- Centralized virtual environment storage in `~/all_venvs`
- Create environments with pip included
- Auto-activate environments in an interactive shell
- List environments with:
  - creation date
  - disk usage
- Rename environments
- Delete environments safely
- Switch between Linux / Windows mode

---

## 📦 Requirements

- Python 3.8+
- `venv` module (bundled with Python)
- (Linux optional) `distro` for nicer OS names

Install `distro` if desired (OPTIONAL) :

```bash
pip install distro
