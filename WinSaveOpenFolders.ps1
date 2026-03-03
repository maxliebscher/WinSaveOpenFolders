Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$SaveFilePath = Join-Path $env:USERPROFILE 'SavedFolders.json'

function Get-OpenExplorerFolders {
    $folders = @(
        (New-Object -ComObject Shell.Application).Windows() |
            Where-Object { $_.Name -in @('Explorer', 'File Explorer') } |
            ForEach-Object {
                try { $_.Document.Folder.Self.Path } catch { $null }
            } |
            Where-Object { $_ -and (Test-Path $_) } |
            Select-Object -Unique
    )
    return $folders
}

function Save-OpenFolders {
    try {
        $openFolders = Get-OpenExplorerFolders
        $openFolders | ConvertTo-Json | Set-Content -Path $SaveFilePath -Encoding UTF8
        [System.Windows.Forms.MessageBox]::Show("Saved $($openFolders.Count) folder(s).", 'Success', 'OK', 'Information') | Out-Null
    }
    catch {
        [System.Windows.Forms.MessageBox]::Show("Failed to save folders:`n$($_.Exception.Message)", 'Error', 'OK', 'Error') | Out-Null
    }
}

function Restore-OpenFolders {
    try {
        if (-not (Test-Path $SaveFilePath)) {
            throw 'No saved folder state found. Please save first.'
        }

        $openFolders = Get-Content -Path $SaveFilePath -Raw | ConvertFrom-Json
        if ($openFolders -isnot [System.Array]) {
            $openFolders = @($openFolders)
        }

        foreach ($folder in $openFolders) {
            Start-Process explorer.exe -ArgumentList $folder
        }

        [System.Windows.Forms.MessageBox]::Show("Restored $($openFolders.Count) folder(s).", 'Success', 'OK', 'Information') | Out-Null
    }
    catch {
        [System.Windows.Forms.MessageBox]::Show("Failed to restore folders:`n$($_.Exception.Message)", 'Error', 'OK', 'Error') | Out-Null
    }
}

$form = New-Object System.Windows.Forms.Form
$form.Text = 'WinSaveOpenFolders'
$form.Size = New-Object System.Drawing.Size(320, 190)
$form.StartPosition = 'CenterScreen'
$form.FormBorderStyle = 'FixedSingle'
$form.MaximizeBox = $false

$label = New-Object System.Windows.Forms.Label
$label.Text = 'WinSaveOpenFolders'
$label.Font = New-Object System.Drawing.Font('Segoe UI', 14)
$label.AutoSize = $true
$label.Location = New-Object System.Drawing.Point(72, 20)
$form.Controls.Add($label)

$saveButton = New-Object System.Windows.Forms.Button
$saveButton.Text = 'Save Open Folders'
$saveButton.Size = New-Object System.Drawing.Size(150, 32)
$saveButton.Location = New-Object System.Drawing.Point(78, 65)
$saveButton.Add_Click({ Save-OpenFolders })
$form.Controls.Add($saveButton)

$restoreButton = New-Object System.Windows.Forms.Button
$restoreButton.Text = 'Restore Open Folders'
$restoreButton.Size = New-Object System.Drawing.Size(150, 32)
$restoreButton.Location = New-Object System.Drawing.Point(78, 105)
$restoreButton.Add_Click({ Restore-OpenFolders })
$form.Controls.Add($restoreButton)

[void]$form.ShowDialog()
