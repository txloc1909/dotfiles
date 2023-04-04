local awful = require("awful")

local tile = awful.layout.suit.tile
local max = awful.layout.suit.max

local _M = {}

function _M.get ()
	awful.screen.connect_for_each_screen(function(s)
		awful.tag.add("One", {
			layout = tile,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Two", {
			layout = tile,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Three", {
			layout = tile,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Four", {
			layout = max,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Five", {
			layout = max,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Six", {
			layout = max,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Seven", {
			layout = max,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Eight", {
			layout = max,
			master_width_factor = 0.55,
			screen = s,
		})
		awful.tag.add("Nine", {
			layout = tile,
			master_width_factor = 0.55,
			screen = s,
		})
		end
	)
end

return setmetatable(
	{},
	{ __call = function(_, ...) return _M.get(...) end }
)
