# premake++
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Wllew4/premake_plus_plus)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Wllew4/premake_plus_plus)
![GitHub](https://img.shields.io/github/license/Wllew4/premake_plus_plus)

Helpful scripts to keep your Premake up-to-date and add additional functionality.

This has not yet been tested on Linux or MacOS, so I cannot confirm that they work on those platforms, though they are expected to.

# Getting started:
1. You must have Python 3 installed on your system.
1. Download the [latest release](https://github.com/Wllew4/premake-plus-plus/releases).
1. Place the `premake_plus_plus/` folder wherever you please, and add it to your system `PATH`.
	* This is where your premake5 installation will live.
1. Open a terminal in `premake_plus_plus/`.
1. Run the `premake_update` script, `.ps1` for Windows and `.sh` for Linux.
	* This will install the latest release of [premake-core](https://github.com/premake/premake-core) to `premake_plus_plus/`.
1. You should now see `premake5.exe` in `premake_plus_plus/`. Congratulations!
1. In order to use the provided actions with your Premake project, you will need to import the module. Add this line to the top of your project's `premake5.lua`:
```lua
require("plus_plus")
```

# Features:
## Keeping Premake up-to-date
Once the `premake_plus_plus` root folder is added to your PATH, Premake can be updated via the terminal from anywhere on your system. This script will pull the latest release of [premake_core](https://github.com/premake/premake-core) from GitHub.
Windows:
```ps1
premake_update
```
Linux:
```sh
premake_update.sh
```
Note that this is a PowerShell/Shell script and NOT a Premake action. You can also update Premake using an action as shown below, but only if your terminal is open to a Premake project with the `plus_plus` module imported.
```
premake5 update
```

## VSCode configuration
Generate `.vscode/c_cpp_properties.json` with:
```
premake5 vscode
```
This will help VSCode intellisense locate included files.

# Planned features:
Premake actions to build VS solutions or from Makefile.
