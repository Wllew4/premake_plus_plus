local p = premake

p.modules.vscode = {}
local m = p.modules.vscode

local projects = {}

newaction {
    trigger = "vscode",
    description = "Generate .vscode folder",

    onProject = function(prj)
        printf("Generating .vscode for project '%s'", prj.name)
        
        projects[#projects+1] = {
            location = prj.location,
            configs = {}
        }

        for config in p.project.eachconfig(prj) do
            project = projects[#projects]
            project.configs[#project.configs+1] = {}
            c = project.configs[#project.configs]
            c.name = config.name
            c.includePath = {}
            c.defines = {}
            for i=1,#config.includedirs do
                c.includePath[i] = config.includedirs[i]
            end
            for i=1,#config.defines do
                c.defines[i] = config.defines[i]
            end
            c.cppStandard = config.cppdialect:lower()
        end
    end,

    onEnd = function()
        for k,v in pairs(projects) do
            local toWrite = {
                configurations = projects[k].configs,
                version = 4
            }
            local writeTo = projects[k].location .. "\\" .. ".vscode\\c_cpp_properties.json"
            io.writefile(writeTo, json.encode(toWrite))
            print(".vscode generation complete.")
        end
    end
}

return m