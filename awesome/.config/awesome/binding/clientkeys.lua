local gears = require("gears")
local awful = require("awful")

local modkey = RC.vars.modkey

local _M = {}

function _M.get ()
	local clientkeys = gears.table.join(
		awful.key({ modkey,           }, "F11",
		    function (c)
			c.fullscreen = not c.fullscreen
			c:raise()
		    end,
		    {description = "toggle fullscreen", group = "client"}),
		awful.key({ modkey,           }, "F4",     function (c) c:kill()                         end,
			  {description = "close", group = "client"}),
		awful.key({ modkey, "Shift"   }, "c",      function (c) c:kill()                         end,
			  {description = "close", group = "client"}),
		awful.key({ modkey, "Control" }, "space",  awful.client.floating.toggle                     ,
			  {description = "toggle floating", group = "client"}),
		awful.key({ modkey, "Control" }, "Return",
                        function (c)
                            local master = awful.client.getmaster()
                            if c ~= master then
                                c:swap(awful.client.getmaster())
                            else
                                awful.client.swap.byidx(1)
                                awful.client.focus.byidx(-1)
                            end
                        end,
			  {description = "move to master (equivalent to dwm's zoom)", group = "client"}),
		-- awful.key({ modkey,           }, "o",      function (c) c:move_to_screen()               end,
		-- 	  {description = "move to screen", group = "client"}),
		awful.key({ modkey, "Shift"   }, "period",  function (c) c:move_to_screen(c.screen.index+1) end,
			  {description = "move to screen", group = "client"}),
		awful.key({ modkey, "Shift"   }, "comma",  function (c) c:move_to_screen(c.screen.index-1) end,
			  {description = "move to screen", group = "client"}),
		awful.key({ modkey,           }, "t",      function (c) c.ontop = not c.ontop            end,
			  {description = "toggle keep on top", group = "client"}),
		awful.key({ modkey,           }, "n",
		    function (c)
			-- The client currently has the input focus, so it cannot be
			-- minimized, since minimized clients can't have the focus.
			c.minimized = true
		    end ,
		    {description = "minimize", group = "client"}),
		awful.key({ modkey,           }, "F10",
		    function (c)
			c.maximized = not c.maximized
			c:raise()
		    end ,
		    {description = "(un)maximize", group = "client"})
	)
	return clientkeys
end

return setmetatable({}, { __call = function(_, ...) return _M.get(...) end })
