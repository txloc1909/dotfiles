local gears = require("gears")
local awful = require("awful")
local naughty = require("naughty")

-- local my_tags = require("main.tags")
local my_tags = RC.tags
local modkey = RC.vars.modkey
local _M = {}


function _M.get (globalkeys)
	for _, my_tag in ipairs(my_tags) do
		globalkeys = gears.table.join(globalkeys,
			-- View tag only
			awful.key({ modkey }, my_tag.key,
				  function ()
					local screen = awful.screen.focused()
					local tag = awful.tag.find_by_name(screen, my_tag.name)
					if tag then
					    tag:view_only()
                                            -- run-or-raise
                                            if #tag:clients() == 0 and tag.main_client then
                                                awful.spawn.single_instance(tag.main_client)
                                            end
					else
					    naughty.notify({
					            title = "Error: View tag only",
					            text = "Tag " .. my_tag.name .. " not found",
					    })
					end
				  end,
				  {description = "view tag #"..my_tag.name, group = "tag"}),
			-- Toggle tag display.
			awful.key({ modkey, "Control" }, my_tag.key,
				  function ()
					local screen = awful.screen.focused()
					local tag = awful.tag.find_by_name(screen, my_tag.name)
					if tag then
					   awful.tag.viewtoggle(tag)
					else
					      naughty.notify({
						      title = "Error: Toggle tag display",
						      text = "Tag " .. my_tag.name .. " not found",
					      })
					end
				  end,
				  {description = "toggle tag #" .. my_tag.name, group = "tag"}),
			-- Move client to tag.
			awful.key({ modkey, "Shift" }, my_tag.key,
				  function ()
					if client.focus then
					     local screen = client.focus.screen
					     local tag = awful.tag.find_by_name(screen, my_tag.name)
					     if tag then
						 client.focus:move_to_tag(tag)
					     else
				        	 naughty.notify({
						      title = "Error: Move client to tag",
						      text = "Tag " .. my_tag.name .. " not found",
						 })
					     end
					end
				  end,
				  {description = "move focused client to tag #"..my_tag.name, group = "tag"}),
			-- Toggle tag on focused client.
			awful.key({ modkey, "Control", "Shift" }, my_tag.key,
				  function ()
				      if client.focus then
					  local screen = client.focus.screen
					  local tag = awful.tag.find_by_name(screen, my_tag.name)
					  if tag then
					      client.focus:toggle_tag(tag)
					  else
				             naughty.notify({
					         title = "Error: Toggle tag on client",
					         text = "Tag " .. my_tag.name .. " not found",
					     })
					  end
				      end
				  end,
				  {description = "toggle focused client on tag #" .. my_tag.name, group = "tag"})
		)
	end
	return globalkeys
end

return setmetatable({}, { __call = function(_, ...) return _M.get(...) end })
