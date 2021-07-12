# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os 
import subprocess

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

mod = "mod4"
terminal = "urxvt"
run_launcher = "rofi -show run"

# Execute autostart script once login
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~") 
    startup_script = home + '/.config/qtile/autostart.sh'
    subprocess.call([startup_script])

# Keybindings
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()), 
    Key([mod], "l", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    #Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    #Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Resize windows 
    Key([mod, "control"], "k", lazy.layout.grow_up()), 
    Key([mod, "control"], "j", lazy.layout.grow_down()), 
    Key([mod, "control"], "h", lazy.layout.grow_left()), 
    Key([mod, "control"], "l", lazy.layout.grow_right()), 
    
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),
    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Spawn the terminal
    Key([mod], "Return", lazy.spawn(terminal)),
    
    # Spawn the run launcher
    Key([mod], "r", lazy.spawn(run_launcher)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # Kill focused window
    Key([mod], "q", lazy.window.kill()),

    # Restart Qtile 
    Key([mod, "shift"], "r", lazy.restart()),
    # Quit Qtile
    Key([mod, "shift"], "q", lazy.shutdown()),
]

groups = [Group(i, layout='monadtall') for i in "123456789"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.MonadTall(), 
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.Floating(), 
]

widget_defaults = dict(
    font='Ubuntu',
    fontsize=14,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.GroupBox(),
                widget.Prompt(),
                widget.CurrentLayoutIcon(),
                widget.CurrentLayout(),
                widget.WindowName(),
                widget.Systray(),
                #widget.MemoryGraph(),
                widget.Memory(fmt='{MemUsed}M/{MemTotal}M'),
                widget.Net(interface='wlp0s20f3'),
                widget.KeyboardLayout(),
                widget.Volume(),
                widget.BatteryIcon(),
                widget.Battery(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            size=25,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "Qtile"
