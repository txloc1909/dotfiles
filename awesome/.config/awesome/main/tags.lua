local awful = require("awful")
local gears = require("gears")
local tyrannical = require("tyrannical")

local tile = awful.layout.suit.tile
local max = awful.layout.suit.max

local _M = {}

local default_tag_opt = {
	selected = false,
	gap = 2,
	master_width_factor = 0.55,
	layout = tile,
}

local my_tags = {
	{
		name            = "Work",
		key             = "u",
                init            = true,
                exclusive       = false,
                layout          = awful.layout.suit.tile,
                -- exec_once       = "org.chromium.Chromium",
                selected        = false,
                class           = { "Chromium-browser" },
                instance        = { "notion.so", "slack", "kitty-workterm" },
	},
	{
		name            = "Term",
		key             = "i",
                init            = true,
                exclusive       = true,
                layout          = awful.layout.suit.tile,
                -- exec_once       = "kitty",
                selected        = false,
                class           = { "kitty", "Gnome-terminal", "kgx", "alacritty" },
                instance        = { "kitty-workterm" },
	},
	{
		name            = "Personal",
		key             = "o",
                init            = true,
                exclusive       = true,
                -- exec_once       = "com.brave.Browser",
                layout          = awful.layout.suit.tile,
                selected        = false,
                instance        = { "brave-browser" },
	},
	{
		name            = "Browse",
		key             = "w",
                init            = true,
                exclusive       = true,
                layout          = awful.layout.suit.tile,
                selected        = false,
                instance        = { "facebook.com", "reddit.com", "brave-browser"},
                class           = { "firefox", "qutebrowser", "Vivaldi-stable" },
	},
	{
		name            = "Chat",
		key             = "e",
                init            = true,
                exclusive       = true,
                -- exec_once       = "org.ferdium.Ferdium",
                layout          = awful.layout.suit.tile,
                selected        = false,
                class           = { "discord", "Caprine", "Skype", "Ferdium" },
	},
	{
		name            = "Vid",
		key             = "y",
                init            = true,
                exclusive       = true,
                -- exec_once       = "flatpak run com.brave.Browser --app=https://youtube.com",
                layout          = awful.layout.suit.max,
                selected        = false,
                class           = { "mpv", "Totem" },
                instance        = { "youtube.com" },
	},
	{
		name            = "Misc",
		key             = "m",
                fallback        = true,
                selected        = false,
                layout          = awful.layout.suit.max,
	}
}

-- tyrannical.settings: keys
-- block_children_focus_stealing
-- force_odd_as_intrusive
-- favor_focused
-- tag
    -- tag.layout
    -- tag.master_width_factor
-- default_layout
-- master_width_factor


function _M.get ()
        tyrannical.settings.default_layout = awful.layout.suit.tile
        tyrannical.settings.master_width_factor = 0.55
        tyrannical.tags = my_tags

        tyrannical.properties.floating = {
            "gnome-calculator",
        }
        tyrannical.properties.centered = {
            "gnome-calculator",
        }

	return my_tags
end

return setmetatable(
	{},
	{ __call = function(_, ...) return _M.get(...) end }
)
