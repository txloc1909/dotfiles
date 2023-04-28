pcall(require, "luarocks.loader")

local gears = require("gears")
local awful = require("awful")
local beautiful = require("beautiful")
local menubar = require("menubar")

RC = {} 	-- global namespaces, on top before require any modules
RC.vars = require("main.variables")

require("main.error_handling")

beautiful.init(gears.filesystem.get_themes_dir() .. "default/theme.lua")
beautiful.border_width = 3

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

awful.layout.layouts = RC.layouts
awful.rules.rules = main.rules(binding.clientkeys(), binding.clientbuttons())

require("awful.autofocus") 	-- automatically focus window when switching tags
require("main.signals")

awful.spawn.with_shell("setxkbmap -option caps:ctrl_modifier")
awful.spawn.once("picom --experimental-backends")
awful.spawn.with_shell("ibus-daemon -drx")
awful.spawn.once("nm-applet")
awful.spawn.with_shell("pgrep volumeicon > /dev/null || volumeicon")
awful.spawn.with_shell("feh --bg-scale " .. RC.vars.wallpaper)
--awful.spawn.once("unclutter") -- already autostart
