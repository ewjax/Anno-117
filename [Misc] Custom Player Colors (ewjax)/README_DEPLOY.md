This repo includes a small PowerShell deployment helper so you can control exactly which files are copied into your game's `mods` folder.

Quick overview
- `deploy.ps1`: Script that copies files from the mod repo to the target mods destination.
- `deploy.json.example`: Example configuration with `include` and `exclude` globs.

How to configure
- Edit `deploy.json` (copy from `deploy.json.example`) and update `include` and `exclude` arrays.
- Patterns are relative to the repo root (or pass `-Source`). Use `**` to match any number of directory levels.

Examples of patterns
- `modinfo.json` — include the mod manifest file
- `data\\**\\*.xml` — include all XML files under `data/` recursively
- `*.html` — include top-level HTML files
- `working\\**` — exclude everything in `working/`

Running the script
From the repo root (PowerShell):

```powershell
# run and specify destination explicitly
.\deploy.ps1 -Source . -Dest "C:\\Program Files\\Anno 1800\\mods\\custom-player-colors-ewjax"

# or rely on deploy.json's `gameModsPath` if present
.\deploy.ps1
```

Notes
- The script preserves relative paths under the destination folder.
- It requires PowerShell (tested with Windows PowerShell 5.1). If you prefer, you can use `robocopy` for simpler folder-based copying.
- If you want me to adjust patterns or add a packaging (zip) step, tell me which behavior you want and I can update the script.
