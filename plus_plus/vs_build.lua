local p = premake

local projects = {}

local vs_versions = {
	"2022"
}

function find_msbuild(vs_version)
	print("Locating MSBuild.exe ...")
	local handle = io.popen("where premake5")
	local result = handle:read("*a")
	handle:close()
	premake_path = string.sub(result, 0, string.len(result) - 14)
	handle = io.popen(
		"Powershell -ExecutionPolicy Unrestricted -File "
		.. premake_path .. "\\plus_plus\\build\\find_msbuild.ps1")
	result = handle:read("*a")
	handle:close()

	-- Confirm file
	if os.isfile(result) then
		return string.sub(result, 0, string.len(result) - 1)
	else
		print("Could not find MSBuild.exe!")
	end
end

function build (vs_version, solution_name)
	-- print(find_msbuild(vs_version))
	command = "\"" .. find_msbuild(vs_version) .. "\" " .. solution_name .. ".sln"
	-- print(command)
	os.execute(command)
end

for i,v in ipairs(vs_versions) do
	newaction {
		trigger = "vs" .. v .. "-build",
		description = "Build a Visual Studio solution.",
	
		onWorkspace = function(wks)
			os.execute("premake5 " .. "vs" .. v)
			build(v, wks.name)
		end
	}
end