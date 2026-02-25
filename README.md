# 🧰 The Manager — Centralized Python Virtual Environment Manager

A command-line tool that creates, stores, manages, and auto-activates Python virtual environments from a single global directory.

Instead of manually tracking environments across projects, all virtual environments are stored in one place and can be listed, renamed, deleted, or activated through an interactive menu.

Supports **Linux and Windows activation modes**.

---

## ✨ Features

- Centralized virtual environment storage in `~/.all_venvs`
- Create environments with pip included
- Auto-activate environments in an interactive shell
- List environments with:
  - creation date
  - disk usage
- Rename environments
- Delete environments safely
- Auto detects operating system and is designed to work on Linux and Windows

---

## 📦 Requirements

- Python 3.8+
- `venv` module (bundled with Python)
- (Linux optional) `distro` for nicer OS names

Install `distro` if desired (OPTIONAL) :

```bash
pip install distro

```

---

## 🚀 Environment Manager

Minimal-dependency CLI tool to create, activate, and track disk usage
of all environments from a single interface.

---

## 📥 Installation

### Clone the repository

```bash
git clone https://github.com/CyberTechNex/The-Manager.git
cd <repo>
```

### Run directly

```bash
python3 manager.py
```

### Make executable (Linux/macOS)

```bash
chmod +x manager.py
```

### (Optional) Add to PATH

```bash
mv manager.py ~/.local/bin/the-manager
```

Run globally:

```bash
the-manager
```

---

## ▶️ Usage

Start the tool:

```bash
python3 manager.py
```

Setup flow:

1. Confirm detected OS  
2. Select activation mode  
3. Enter main menu

---

## 📂 Main Menu

| Option | Action |
|-------:|--------|
| **[1]** | List / Manage environments |
| **[2]** | Create new environment |
| **[3]** | Change OS Mode |
| **[4]** | Quit |

---

## 🗂 List & Manage

```
#   Name         Created        Disk Usage
1   myproject    03 Jan 2026    142.8 MB
2   testenv      02 Jan 2026     85.3 MB
```

Actions:

- **y** → activate
- **r** → rename
- **del** → delete
- **n** → back

---

## ⚡ Auto-Activation Behavior

### Linux Mode
- Detects `$SHELL`
- Sources `bin/activate`
- Opens interactive session

### Windows Mode
- Uses `Scripts\activate`
- Opens `cmd.exe` with venv active

---

## ➕ Create New Environment

The tool:

1. Prompts for name  
2. Creates venv in `~/.all_venvs/<name>`  
3. Installs pip  
4. Auto-activates immediately

---

## 🔁 Change OS Mode

Useful for:

- WSL
- Dual-boot systems
- Shared drives
- Wrong system OS detection (very rare)

---

## 🧠 Design Notes

- **Centralized** — no scattered `.venv` folders  
- **Minimalist** — `venv.EnvBuilder(with_pip=True)`  
- **Data-Driven** — filesystem `ctime` + recursive disk usage  
- **Robust** — `shutil.rmtree` + graceful missing-path handling  

---
