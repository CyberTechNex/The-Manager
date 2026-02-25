#!/usr/bin/env python3

import os
import sys
import shutil
import venv
import platform
from pathlib import Path
from datetime import datetime


# ---------- CONFIG ----------
BASE_DIR = Path.home() / ".all_venvs"
BASE_DIR.mkdir(exist_ok=True)


# ---------- BANNER ----------
def banner():
    RESET = "\033[0m"
    BOLD = "\033[1m"
    TITLE = "\033[33m"
    TAG = "\033[36m"

    print(rf"""
{BOLD}{TITLE}=== THE MANAGER ==={RESET}

{TAG}Only noobs manually activate their enviorments{RESET}
""")


# ---------- OS DETECTION ----------
def detect_os_string():
    system = platform.system().lower()

    if "linux" in system:
        try:
            import distro
            name = distro.name(pretty=True) or "Linux"
            ver = distro.version(best=True) or ""
            return f"{name} {ver}".strip()
        except Exception:
            return platform.platform()

    if "windows" in system:
        return f"Windows {platform.version()}"

    return platform.platform()


def choose_os():
    detected = platform.system()

    print("\nSystem detected is:", detect_os_string())
    print("\nSelect OS Mode:\n")

    if detected.lower() == "linux":
        print("[1] Linux (recommended)")
        print("[2] Windows")
    else:
        print("[1] Linux")
        print("[2] Windows (recommended)")

    print("[3] Quit\n")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        return "Linux"
    if choice == "2":
        return "Windows"
    if choice == "3":
        print("\nExiting...\n")
        sys.exit(0)

    print("\nInvalid choice — using detected mode.\n")
    return "Linux" if detected.lower() == "linux" else "Windows"


# ---------- UTILITIES ----------
def folder_size(path: Path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                total += (Path(root) / f).stat().st_size
            except FileNotFoundError:
                pass
    return total


def fmt_size(bytes_val):
    return f"{bytes_val / (1024*1024):.2f} MB"


# ---------- VENV LIST ----------
def list_venvs():
    venvs = []

    for p in BASE_DIR.iterdir():
        if not p.is_dir():
            continue

        created = datetime.fromtimestamp(
            p.stat().st_ctime
        ).strftime("%d %b %Y")

        size = fmt_size(folder_size(p))

        venvs.append((p.name, p, created, size))

    return sorted(venvs)


def print_table(venvs):
    print(f"\nVenvs in {BASE_DIR}:\n")
    print("{:<3} {:<28} {:<14} {:<12}".format("#", "Name", "Created", "Disk Usage"))
    print("-" * 60)

    for i, (name, _, created, size) in enumerate(venvs, 1):
        print("{:<3} {:<28} {:<14} {:<12}".format(i, name, created, size))

    print()


# ---------- AUTO ACTIVATE ----------
def activate_env(path: Path, os_mode):
    if os_mode == "Windows":
        script = path / "Scripts" / "activate"
        cmd = f"{script}"
        os.execvp("cmd.exe", ["cmd.exe", "/K", cmd])

    else:
        script = path / "bin" / "activate"
        shell = os.environ.get("SHELL", "/bin/bash")
        os.execvp(shell, [shell, "-i", "-c", f"source '{script}' && exec {shell} -i"])


# ---------- CREATE ----------
def create_venv(os_mode):
    name = input("\nEnter environment name: ").strip()
    if not name:
        print("Invalid name.")
        return

    path = BASE_DIR / name

    if path.exists():
        print("Environment already exists.")
        return

    print("\nCreating environment...")
    venv.EnvBuilder(with_pip=True).create(path)

    print("Created:", path)
    print("\nActivating...\n")

    activate_env(path, os_mode)


# ---------- RENAME ----------
def rename_env(path: Path, old_name):
    new_name = input("Enter new name: ").strip()

    if not new_name:
        print("Invalid name.")
        return

    new_path = BASE_DIR / new_name

    if new_path.exists():
        print("A venv with that name already exists.")
        return

    shutil.move(path, new_path)

    print(f"Renamed {old_name} → {new_name}")


# ---------- DELETE ----------
def delete_env(path: Path, name):
    confirm = input(f"Delete {name}? (y/n): ").strip().lower()

    if confirm == "y":
        shutil.rmtree(path, ignore_errors=True)
        print("Deleted.")
    else:
        print("Cancelled.")


# ---------- SELECT / MANAGE ----------
def manage_env(os_mode):
    venvs = list_venvs()

    if not venvs:
        print("\nNo environments found.\n")
        create_now = input("Create one? (y/n): ").strip().lower()
        if create_now == "y":
            create_venv(os_mode)
        return

    print_table(venvs)

    choice = input("Select environment number: ").strip()
    if not choice.isdigit():
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(venvs):
        return

    name, path, _, _ = venvs[idx]

    while True:
        print(f"\nSelected: {name}")
        print("[y] Activate")
        print("[r] Rename")
        print("[del] Delete")
        print("[n] Back\n")

        action = input("Choose: ").strip().lower()

        if action == "y":
            print("\nActivating...\n")
            activate_env(path, os_mode)

        elif action == "r":
            rename_env(path, name)
            return

        elif action == "del":
            delete_env(path, name)
            return

        elif action == "n":
            return


# ---------- MAIN ----------
def main():
    banner()

    os_mode = choose_os()

    while True:
        print("\nMain Menu\n")
        print("[1] List / Manage environments")
        print("[2] Create new environment")
        print("[3] Change OS Mode")
        print("[4] Quit\n")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            manage_env(os_mode)

        elif choice == "2":
            create_venv(os_mode)

        elif choice == "3":
            os_mode = choose_os()

        elif choice == "4":
            print("\nGoodbye.\n")
            sys.exit(0)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
