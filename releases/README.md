# Releases

This folder contains release templates and notes for GitHub releases.

## Typical release asset
- `WinSaveOpenFolders-windows.zip`
  - `WinSaveOpenFolders.exe`
  - `LICENSE`
  - `README.md`

## Recommended release process
1. Push to `main` to let GitHub Actions build the latest EXE.
2. Download the workflow artifact from the **Actions** tab.
3. For a public versioned release, create a tag like `v1.0.0` and push it.
4. The workflow will automatically create a GitHub Release and attach the ZIP file.
