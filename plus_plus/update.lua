newaction {
    trigger = "update",
    description = "Update premake",

	onStart = function()
		local handle
		if package.config:sub(1,1) == '\\' then
			handle = io.popen("where premake5")
		elseif package.config:sub(1,1) == '/' then
			handle = io.popen("which premake5")
		else
			print("Unable to determine system type. Cannot determine installation location.")
		end
		
		local result = handle:read("*a")
		handle:close()
		premake_path = string.sub(result, 0, string.len(result) - 14)
		os.execute("cd " .. premake_path .. " && python plus_plus/update/update.py")
	end
}