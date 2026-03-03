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
- **GitHub Actions EXE build** → automatic Windows `.exe` build after push

## Features
- Saves all currently open Windows File Explorer windows to a JSON file
- Restores the saved folders with one click
- Very small and simple GUI
- No Python required for the PowerShell launcher version
- Optional automatic `.exe` build via GitHub Actions

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

## Automatic EXE build with GitHub Actions
After pushing this repository to GitHub:

1. Open the **Actions** tab.
2. Run or wait for **Build Windows EXE**.
3. Download the artifact **WinSaveOpenFolders-windows**.
4. If you push a tag like `v1.0.0`, GitHub will also create a release ZIP automatically.

No local build tools are required for that workflow.

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
