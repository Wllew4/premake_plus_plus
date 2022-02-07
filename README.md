# premake++
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Wllew4/premake_plus_plus)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Wllew4/premake_plus_plus)
![GitHub](https://img.shields.io/github/license/Wllew4/premake_plus_plus)

Helpful Premake actions for updating, etc.

This has not yet been tested on Linux or MacOS, so I cannot confirm that they work on those platforms, though they are expected to.

# Getting started:
1. You must have Python 3 installed on your system.
1. Download the [latest release](https://github.com/Wllew4/premake-plus-plus/releases).
1. Place the `premake_plus_plus/` folder wherever you please, and add it to your system `PATH`.
	* This is where your premake5 installation will live.
1. Open a terminal `premake_plus_plus/`.
1. Run `python install.py`.
	* This will install the latest release of [premake-core](https://github.com/premake/premake-core) to `premake_plus_plus/`.
1. You should now see `premake5.exe` in `premake_plus_plus/`. Congratulations!
1. In order to use the provided actions with your Premake project, you will need to import the module. Add this line to the top of your project's `premake5.lua`:
```lua
require("plus_plus")
```

# Features:
## Keeping Premake up-to-date
To replace your `premake5.exe` with the latest release available on GitHub, run this action:
```
premake5 update
```

## VSCode configuration
Generate `.vscode/c_cpp_properties.json` with:
```
premake5 vscode
```
This will help intellisense locate included files and available STL features.

# Planned features:
Premake actions to build VS solutions or from Makefile.
