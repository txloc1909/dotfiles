local awful = require("awful")

local _M = {}

function _M.get () 
	tags = {}
	awful.screen.connect_for_each_screen(function(s)
		tags[s] = awful.tag(
			{ "1", "2", "3", "4", "5", "6", "7", "8", "9" }, s, RC.layouts[1]
		)
		end
	)
end

return setmetatable(
	{},
	{ __call = function(_, ...) return _M.get(...) end }
)

