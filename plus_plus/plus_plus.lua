local p = premake

p.modules.plus_plus = {}
local m = p.modules.plus_plus

require "update"
require "vscode"
require "vs_build"

return m