import os
import json
import subprocess
from pathlib import Path
from tkinter import Tk, Button, Label, messagebox

# Define paths for saving and restoring folder states
save_file_path = Path.home() / "SavedFolders.json"

def save_open_folders():
    """Save currently open folders to a file."""
    try:
        shell = subprocess.Popen(
            ["powershell", "-Command", "(New-Object -ComObject Shell.Application).Windows() | Where-Object { $_.Name -eq 'Explorer' } | ForEach-Object { $_.Document.Folder.Self.Path }"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = shell.communicate()

        if shell.returncode == 0:
            open_folders = [line.strip() for line in stdout.splitlines() if line.strip()]
            with open(save_file_path, 'w', encoding='utf-8') as save_file:
                json.dump(open_folders, save_file, ensure_ascii=False, indent=4)
            messagebox.showinfo("Success", f"Saved {len(open_folders)} folder(s).")
        else:
            raise Exception(stderr)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save folders: {e}")

def restore_open_folders():
    """Restore folders from the saved file."""
    try:
        if not save_file_path.exists():
            raise FileNotFoundError("No saved folder state found. Please save first.")

        with open(save_file_path, 'r', encoding='utf-8') as save_file:
            open_folders = json.load(save_file)

        for folder in open_folders:
            subprocess.Popen(["explorer", folder])

        messagebox.showinfo("Success", f"Restored {len(open_folders)} folder(s).")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to restore folders: {e}")

# Create a simple GUI
def create_gui():
    root = Tk()
    root.title("WinSaveOpenFolders")
    root.geometry("300x150")

    Label(root, text="WinSaveOpenFolders", font=("Helvetica", 14)).pack(pady=10)

    Button(root, text="Save Open Folders", command=save_open_folders, width=20).pack(pady=5)
    Button(root, text="Restore Open Folders", command=restore_open_folders, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
