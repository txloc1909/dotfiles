local awful = require("awful")
local gears = require("gears")

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
		name = "Work",
		key = "u",
		opt = { }
	},
	{
		name = "Term",
		key = "i",
		opt = { }
	},
	{
		name = "Personal",
		key = "o",
		opt = { }
	},
	{
		name = "Browse",
		key = "w",
		opt = {
			layout = tile,
		}
	},
	{
		name = "Chat",
		key = "e",
		opt = {
			layout = tile,
			master_width_factor = 0.6,
		}
	},
	{
		name = "Vid",
		key = "y",
		opt = {
			layout = max
		}
	},
	{
		name = "Misc",
		key = "m",
		opt = {
			layout = max
		}
	}
}

function _M.get ()
	awful.screen.connect_for_each_screen(function(s)
		for _, my_tag in ipairs(my_tags) do
			awful.tag.add(my_tag.name,
				gears.table.join(default_tag_opt, my_tag.opt, { screen = s })
			)
		end
	end)

	return my_tags
end

return setmetatable(
	{},
	{ __call = function(_, ...) return _M.get(...) end }
)
