# premake++
A lightweight version manager for Premake that comes with some additional scripts.

## Features:
```
python update.py
```
Will update your premake5.exe to the latest version
or download the latest version if it is not found in
your PATH.

In premake5.lua
```lua
require('vscode')
```
Will allow you to run
```
premake5 vscode
```
which will generate `.vscode/c_cpp_properties.json`.

## Planned features:
Premake actions to build vs solutions or from makefile.