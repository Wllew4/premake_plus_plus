newaction {
    trigger = "update",
    description = "Update premake",

	onStart = function()
		if package.config:sub(1,1) == '\\' then
			local handle = io.popen("where premake5")
			local result = handle:read("*a")
			handle:close()
			premake_path = string.sub(result, 0, string.len(result) - 14)
			os.execute("cd " .. premake_path .. " && python plus_plus/update.py")
		end
	end
}