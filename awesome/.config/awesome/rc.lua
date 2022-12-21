pcall(require, "luarocks.loader")

local gears = require("gears")
local awful = require("awful")
local beautiful = require("beautiful")
local menubar = require("menubar")

RC = {} 	-- global namespaces, on top before require any modules
RC.vars = require("main.variables")

require("main.error_handling")

beautiful.init(gears.filesystem.get_themes_dir() .. "default/theme.lua")

terminal   = RC.vars.terminal
editor     = RC.vars.editor
editor_cmd = terminal .. " -e " .. editor
modkey 	   = RC.vars.modkey

local main = {
	layouts = require("main.layouts"),
	tags    = require("main.tags"),
	menu    = require("main.menu"),
	rules   = require("main.rules"),
}

RC.layouts = main.layouts()
RC.tags = main.tags()
RC.mainmenu = awful.menu({ items = main.menu() })
RC.launcher = awful.widget.launcher(
	{ image = beautiful.awesome_icon, menu = RC.mainmenu }
)
menubar.utils.terminal = RC.vars.terminal

require("deco.statusbar")

local binding = {
	globalbuttons = require("binding.globalbuttons"),
	clientbuttons = require("binding.clientbuttons"),
	globalkeys = require("binding.globalkeys"),
	bindtotags = require("binding.bindtotags"),
	clientkeys = require("binding.clientkeys"),
}

RC.globalkeys = binding.globalkeys()
RC.globalkeys = binding.bindtotags(RC.globalkeys)

root.buttons(binding.globalbuttons())
root.keys(RC.globalkeys)

awful.rules.rules = main.rules(binding.clientkeys(), binding.clientbuttons())

require("awful.autofocus") 	-- automatically focus window when switching tags
require("main.signals")
