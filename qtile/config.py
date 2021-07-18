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
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


##################################################################
#                             VARIABLES                          #
##################################################################

mod = "mod4"
alt = "mod1"
terminal = "urxvt" 
run_launcher = "rofi -show run"
web_browser = "firefox"

# Color scheme
monokai = {
    "background": "272822",             # black/grey-ish
    "foreground": "f8f8f2",             # white & yellow-ish
    "comment": "75715e",                # grey & yellow-ish
    "red": "f92672",
    "orange": "fd971f",
    "light orange": "e69f66",
    "yellow": "e6db74",
    "green": "a6e22e",
    "blue": "66d9ef",
    "purple": "ae81ff",
}

colors = {
    "white": "ffffff",
    "black": "000000",
}

##################################################################
#                           KEYBINDINGS                          #
##################################################################

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Arrow keys do the same 
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Arrow keys do the same
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), 
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc="Toggle maximum size"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), 
        desc="Grow window up"),
 
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Kill focused windows
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Spawn programs 
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn(run_launcher), desc="Spawn the run launcher"),
    Key([mod], "b", lazy.spawn(web_browser), desc="Spawn the web browser"),

    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"),
            desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"),
            desc="Decrease brightness"),
]

##################################################################
#                            GROUPS                              #
##################################################################

groups = [Group(i, layout="monadtall") for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        ])

##################################################################
#                           LAYOUTS                              #
##################################################################

# Default theme for layouts
layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": monokai["purple"],
    "border_normal": monokai["comment"],
}

layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme),
]

##################################################################
#                              BARS                              #
##################################################################

# Default theme for widgets & extensions
widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=3,
    background=monokai["background"],
)
extension_defaults = widget_defaults.copy()

def init_primary_bar():
    return bar.Bar(
        widgets=[
            widget.GroupBox(),
            widget.Prompt(),
            widget.CurrentLayoutIcon(),
            widget.CurrentLayout(),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Spacer(),
            widget.Clock(format='%a %d/%m/%Y %I:%M %p'),
            widget.Spacer(),
            widget.CPU(format="CPU {load_percent:2}%"),
            widget.Memory(format="{MemUsed:5}M/{MemTotal:5}M"),
            widget.Net(
                interface="wlp0s20f3",
                format="{down:6.6} ↓↑ {up:6.6}",
                ),
            widget.KeyboardLayout(),
            widget.Volume(),
            widget.Sep(),
            widget.BatteryIcon(),
            widget.Battery(format="{percent:2.0%}"),
            widget.Sep(),
            widget.Systray(),
        ],
        size=25,
)

def init_secondary_bar():
    pass

##################################################################
#                           SCREENS                              #
##################################################################

screens = [
    Screen(
        top=init_primary_bar(),    
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
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Execute autostart script once login
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~") 
    startup_script = home + '/.config/qtile/autostart.sh'
    subprocess.call([startup_script])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "Qtile"
