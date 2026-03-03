# WinSaveOpenFolders

Small Windows utility to **save** and **restore** currently open File Explorer folders.

![Screenshot](assets/screenshot.jpg)

## Features
- Saves all currently open Windows File Explorer windows to a JSON file
- Restores the saved folders with one click
- Simple Tkinter GUI

## Requirements
- Windows
- Python 3.x
- PowerShell

## Run
```bash
python WinSaveOpenFolders.py
```

## Note
Saved folders are stored here:

```text
%USERPROFILE%\SavedFolders.json
```

## Tech Stack
- `tkinter` for the interface
- `powershell` to read open Explorer windows
- `explorer` to reopen saved folders
