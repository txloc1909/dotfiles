local awful = require("awful")
local gears = require("gears")

local tile = awful.layout.suit.tile
local max = awful.layout.suit.max

local _M = {}

local default_tag_opt = {
	master_width_factor = 0.55,
	layout = tile,
}

local my_tags = {
	{
		name = "U",
		key = "u",
		opt = { }
	},
	{
		name = "I",
		key = "i",
		opt = { }
	},
	{
		name = "O",
		key = "o",
		opt = { }
	},
	{
		name = "(W)eb",
		key = "w",
		opt = {
			layout = max,
		}
	},
	{
		name = "(E)nt",
		key = "e",
		opt = {
			layout = tile,
			master_width_factor = 0.6,
		}
	},
	{
		name = "(Y)outube",
		key = "y",
		opt = {
			layout = max
		}
	},
	{
		name = "(M)ess",
		key = "m",
		opt = { }
	},
	{
		name = "(N)ote",
		key = "n",
		opt = {
			layout = tile,
			volatile = true,
		}
	},
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
