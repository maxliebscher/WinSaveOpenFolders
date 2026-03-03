# WinSaveOpenFolders

Small Windows utility to **save** and **restore** currently open File Explorer folders.

![Screenshot](assets/screenshot.jpg)

## Best option for end users
Use the included **`WinSaveOpenFolders.cmd`** launcher.

That version starts the bundled **PowerShell GUI** and works on a standard Windows system **without installing Python or any dependencies**.

## Included versions
- **`WinSaveOpenFolders.cmd`** → easiest option for regular users
- **`WinSaveOpenFolders.ps1`** → native PowerShell GUI implementation
- **`WinSaveOpenFolders.py`** → Python version

## Features
- Saves all currently open Windows File Explorer windows to a JSON file
- Restores the saved folders with one click
- Very small and simple GUI
- No Python required for the PowerShell launcher version

## Run
### No-install Windows version
Double-click:

```text
WinSaveOpenFolders.cmd
```

### PowerShell version
```powershell
powershell -ExecutionPolicy Bypass -File .\WinSaveOpenFolders.ps1
```

### Python version
```bash
python WinSaveOpenFolders.py
```

## Requirements
### For the no-install version
- Windows
- PowerShell (included with Windows)

### For the Python version
- Windows
- Python 3.x
- PowerShell

## Saved file location
```text
%USERPROFILE%\SavedFolders.json
```

## Notes
- The app only stores folder paths.
- If Windows SmartScreen or script warnings appear, you may need to confirm that you want to run the file.
- The `.cmd` launcher calls the PowerShell script with `-ExecutionPolicy Bypass` so it is easier for non-technical users to start.

## License
MIT
