import json
import subprocess
import sys
from pathlib import Path
from tkinter import Tk, Button, Label, messagebox

SAVE_FILE_PATH = Path.home() / 'SavedFolders.json'


def resource_path(relative_path: str) -> Path:
    base_path = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
    return base_path / relative_path


def get_open_explorer_folders() -> list[str]:
    """Return a unique list of currently open File Explorer folder paths."""
    command = (
        "(New-Object -ComObject Shell.Application).Windows() "
        "| Where-Object { $_.Name -in @('Explorer', 'File Explorer') } "
        "| ForEach-Object { try { $_.Document.Folder.Self.Path } catch {} }"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        check=True,
    )
    folders = []
    for line in result.stdout.splitlines():
        path = line.strip()
        if path and path not in folders:
            folders.append(path)
    return folders


def save_open_folders() -> None:
    try:
        open_folders = get_open_explorer_folders()
        with open(SAVE_FILE_PATH, 'w', encoding='utf-8') as save_file:
            json.dump(open_folders, save_file, ensure_ascii=False, indent=2)
        messagebox.showinfo('Success', f'Saved {len(open_folders)} folder(s).')
    except Exception as exc:
        messagebox.showerror('Error', f'Failed to save folders:\n{exc}')


def restore_open_folders() -> None:
    try:
        if not SAVE_FILE_PATH.exists():
            raise FileNotFoundError('No saved folder state found. Please save first.')

        with open(SAVE_FILE_PATH, 'r', encoding='utf-8') as save_file:
            open_folders = json.load(save_file)

        for folder in open_folders:
            subprocess.Popen(['explorer', folder])

        messagebox.showinfo('Success', f'Restored {len(open_folders)} folder(s).')
    except Exception as exc:
        messagebox.showerror('Error', f'Failed to restore folders:\n{exc}')


def create_gui() -> None:
    root = Tk()
    root.title('WinSaveOpenFolders')
    root.geometry('300x150')
    root.resizable(False, False)

    try:
        icon_path = resource_path('assets/icon.ico')
        if icon_path.exists():
            root.iconbitmap(default=str(icon_path))
    except Exception:
        pass

    Label(root, text='WinSaveOpenFolders', font=('Segoe UI', 14)).pack(pady=10)
    Button(root, text='Save Open Folders', command=save_open_folders, width=20).pack(pady=5)
    Button(root, text='Restore Open Folders', command=restore_open_folders, width=20).pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    create_gui()
