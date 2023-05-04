local awful = require("awful")
local tyrannical = require("tyrannical")

local _M = {}

local default_tag_opt = {
	selected = false,
	gap = 2,
	master_width_factor = 0.55,
	layout = awful.layout.suit.tile,
}

local my_tags = {
	{
		name            = "Work",
		key             = "u",
                init            = true,
                exclusive       = false,
                layout          = awful.layout.suit.tile,
                main_client     = "org.chromium.Chromium",
                selected        = false,
                screen          = {1, 2},
                class           = { "Chromium-browser", "Slack" },
                instance        = { "notion.so", "slack", "kitty-workterm" },
                gap = 2,
	},
	{
		name            = "Term",
		key             = "i",
                init            = true,
                exclusive       = true,
                layout          = awful.layout.suit.tile,
                main_client     = "kitty",
                selected        = false,
                screen          = {1, 2},
                class           = { "kitty", "Gnome-terminal", "kgx", "alacritty" },
                gap = 2,
	},
	{
		name            = "Personal",
		key             = "o",
                init            = true,
                exclusive       = true,
                main_client     = "com.brave.Browser",
                layout          = awful.layout.suit.tile,
                selected        = false,
                screen          = {1, 2},
                instance        = { "brave-browser" },
                gap = 2,
	},
	{
		name            = "Browse",
		key             = "w",
                init            = true,
                exclusive       = true,
                layout          = awful.layout.suit.tile,
                selected        = false,
                screen          = {1, 2},
                instance        = { "facebook.com", "reddit.com", "brave-browser"},
                class           = { "firefox", "qutebrowser", "Vivaldi-stable" },
                gap = 2,
	},
	{
		name            = "Chat",
		key             = "e",
                init            = true,
                exclusive       = true,
                main_client     = "com.sindresorhus.Caprine",
                layout          = awful.layout.suit.tile,
                selected        = false,
                screen          = {1, 2},
                class           = { "discord", "Caprine", "Skype", "Ferdium" },
                gap = 2,
	},
	{
		name            = "Vid",
		key             = "y",
                init            = true,
                exclusive       = true,
                main_client     = "youtube",
                layout          = awful.layout.suit.max,
                selected        = false,
                screen          = {1, 2},
                class           = { "mpv", "Totem" },
                instance        = { "youtube.com" },
	},
	{
		name            = "Misc",
		key             = "m",
                fallback        = true,
                selected        = false,
                screen          = {1, 2},
                layout          = awful.layout.suit.max,
                gap = 2,
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
