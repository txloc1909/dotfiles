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
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

import arcobattery                      # battery widget from ArcoLinux


##################################################################
#                             VARIABLES                          #
##################################################################

mod = "mod4"                            # Super/Window key
alt = "mod1"                            # Alt key
# terminal = "urxvtc"                     # use urxvt client
terminal = "alacritty"
run_launcher = "rofi -modi run,drun -show drun"
#run_launcher = "dmenu_run"
web_browser = "firefox"
file_manager = "pcmanfm"
home = os.path.expanduser("~")          # home directory

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
    "blue": "4f76c7",
    "violet": "74438f",
    "red": "ff5555",
    "green": "55ff55",
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
    # Old habit from Windows and Ubuntu
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to next window"),
    Key([alt, "shift"], "Tab", lazy.layout.previous(),
        desc="Move window focus to previous window"),

    # Arrow keys do the same
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),     # in COLUMNS layout
        lazy.layout.swap_left(),        # in MONADTALL layout
        desc="Move window to the left"),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Arrow keys do the same
    Key([mod, "shift"], "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left().when(layout="columns"),        # in COLUMNS layout
        lazy.layout.shrink().when(layout="monadtall"),           # in MONADTALL layout
        desc="Grow window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right().when(layout="columns"),
        lazy.layout.grow().when(layout="monadtall"),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),

    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
        desc="Grow window up"),

    Key([mod], "n",
        lazy.layout.normalize(),        # in COLUMNS layout
        lazy.layout.reset(),            # in MONADTALL layout
        desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc="Toggle maximum size"),

    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen(),
        desc="Make window fullscreen"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),
        desc="Switch to next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(),
        desc="Switch to previous layout"),

    # Kill focused windows
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod, "shift"], "e", lazy.spawn("light-locker-command -l"),
        desc="Lock the screen"),

    # Multi monitors operation
    Key([mod], "p", lazy.next_screen(), desc="Move focus to next monitor"),

    # Spawn programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn(run_launcher), desc="Spawn the run launcher"),
    Key([mod], "w", lazy.spawn(web_browser), desc="Spawn the web browser"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Spawn the file manager"),

    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"),
            desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"),
            desc="Decrease brightness"),

    # Sound control
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"),
            desc="Mute audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"),
            desc="Decrease volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5"),
            desc="Increase volume"),

    # Move visually between groups
    Key([mod, alt], "h", lazy.screen.prev_group(),
        desc="Move to previous group in line"),
    Key([mod, alt], "l", lazy.screen.next_group(),
        desc="Move to next group in line"),
    # Arrow keys do the same thing
    Key([mod, alt], "Left", lazy.screen.prev_group(),
        desc="Move to previous group in line"),
    Key([mod, alt], "Right", lazy.screen.next_group(),
        desc="Move to next group in line"),
]

##################################################################
#                            GROUPS                              #
##################################################################

# group_icons = ['', '', '', '', '', '', '', '', '阮']
# groups = [
    # Group(
        # name=str(i)+":"+icon,
        # layout="monadtall",
    # )
    # for i, icon in enumerate(group_icons, start=1)
# ]

groups = [Group(i, layout="columns") for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + group's number = switch to group
        Key([mod], i.name[0], lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + group's number = switch to & move focused window to group
        Key([mod, "shift"], i.name[0], lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        ])

##################################################################
#                           LAYOUTS                              #
##################################################################

# Default theme for layouts
layout_theme = {
    "border_width": 4,
    "margin": 10,
    "border_focus": colors["green"],
    "border_normal": colors["black"],
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(
        border_focus_stack=monokai["green"],
        border_normal_stack=monokai["background"],
        insert_position=1,
        **layout_theme
    ),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
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
    #font='Ubuntu Mono',
    font='MesloLGS NF',
    fontsize=14,
    padding=3,
    background=monokai["background"],
)
extension_defaults = widget_defaults.copy()

def init_primary_widget_list():
    return [
        #widget.Image(
        #    filename="~/.config/qtile/python-white.png",
        #    scale=True,
        #    margin=3,
        #),
        widget.TextBox(
            text="  ",
            fontsize=24,
            padding=0,
            foreground=colors["white"],
            background=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=colors["black"],
            background=colors["blue"],
        ),
        widget.Sep(
            background=colors["blue"],
            linewidth=0,
            padding=5,
        ),
        widget.GroupBox(
            active="ffffff",
            inactive="ecbbfb",
            highlight_method="line",
            highlight_color=colors["violet"],
            this_current_screen_border="e1acff",
            this_screen_border="74438f",
            other_current_screen_border="e1acff",
            other_screen_border="74438f",
            margin_x=0,
            margin_y=3,
            padding_y=5,
            padding_x=3,
            border_width=3,
            disable_drag=True,
            background=colors["blue"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=colors["blue"],
            background=colors["violet"],
        ),
        widget.CurrentLayoutIcon(
            scale=0.75,
            background=colors["violet"],
        ),
        widget.CurrentLayout(
            background=colors["violet"],
            foreground=colors["white"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=colors["violet"],
        ),
        #widget.Chord(
        #    chords_colors={
        #        'launch': ("#ff0000", "#ffffff"),
        #    },
        #    name_transform=lambda name: name.upper(),
        #),
        widget.WindowName(
            max_chars=20,
            padding=10,
            #for_current_screen=True,
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["red"],
        ),
        widget.CPU(
            format="  {load_percent:2}% ",
            background=monokai["red"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["blue"],
            background=monokai["red"],
        ),
        widget.Memory(
            format="{MemUsed:5.0f}M/{MemTotal:5.0f}M ",
            background=monokai["blue"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["purple"],
            background=monokai["blue"],
        ),
        widget.Net(
            interface="wlp0s20f3",
            format=" {down} ↓↑ {up} ",
            background=monokai["purple"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["orange"],
            background=monokai["purple"],
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            brightness_file="brightness",
            max_brightness_file="max_brightness",
            format="☼ {percent:2.0%} ",
            foreground=colors["black"],
            background=monokai["orange"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["green"],
            background=monokai["orange"],),
        #widget.BatteryIcon(),
        arcobattery.BatteryIcon(
            padding=0,
            scale=0.7,
            y_poss=2,
            theme_path=home+"/.config/qtile/battery_icons_horiz",
            update_interval=5,
            background=monokai["green"],
        ),
        widget.Battery(
            #format="  {percent:2.0%} ",
            format="{percent:2.0%} ",
            background=monokai["green"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            foreground=colors["blue"],
            background=monokai["green"],
            padding=0,
        ),
        widget.Clock(
            format=' %a %d/%m/%Y %H:%M',
            background=colors["blue"],
            foreground=colors["white"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["light orange"],
            background=colors["blue"],
        ),
        widget.Systray(
            background=monokai["light orange"],
        ),
]

def init_secondary_widget_list():
    return [
        widget.Sep(
            background=colors["blue"],
            linewidth=0,
            padding=5,
        ),
        widget.GroupBox(
            active="ffffff",
            inactive="ecbbfb",
            highlight_method="line",
            highlight_color=colors["violet"],
            this_current_screen_border="e1acff",
            this_screen_border="74438f",
            other_current_screen_border="e1acff",
            other_screen_border="74438f",
            margin_x=0,
            margin_y=3,
            padding_y=5,
            padding_x=3,
            border_width=3,
            disable_drag=True,
            background=colors["blue"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=colors["blue"],
            background=colors["violet"],
        ),
        widget.CurrentLayoutIcon(
            scale=0.75,
            background=colors["violet"],
        ),
        widget.CurrentLayout(
            background=colors["violet"],
            foreground=colors["white"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=colors["violet"],
        ),
        #widget.Chord(
        #    chords_colors={
        #        'launch': ("#ff0000", "#ffffff"),
        #    },
        #    name_transform=lambda name: name.upper(),
        #),
        widget.WindowName(
            max_chars=20,
            padding=10,
            #for_current_screen=True,
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["red"],
        ),
        widget.CPU(
            format="  {load_percent:2}% ",
            background=monokai["red"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["blue"],
            background=monokai["red"],
        ),
        widget.Memory(
            format="{MemUsed:5.0f}M/{MemTotal:5.0f}M ",
            background=monokai["blue"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["purple"],
            background=monokai["blue"],
        ),
        widget.Net(
            interface="wlp0s20f3",
            format=" {down} ↓↑ {up} ",
            background=monokai["purple"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["orange"],
            background=monokai["purple"],
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            brightness_file="brightness",
            max_brightness_file="max_brightness",
            format="☼ {percent:2.0%} ",
            foreground=colors["black"],
            background=monokai["orange"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            padding=0,
            foreground=monokai["green"],
            background=monokai["orange"],
        ),
        arcobattery.BatteryIcon(
            padding=0,
            scale=0.7,
            y_poss=2,
            theme_path=home+"/.config/qtile/battery_icons_horiz",
            update_interval=5,
            background=monokai["green"],
        ),
        widget.Battery(
            format="{percent:2.0%} ",
            background=monokai["green"],
            foreground=colors["black"],
        ),
        widget.TextBox(
            text="",
            fontsize=18,
            foreground=colors["blue"],
            background=monokai["green"],
            padding=0,
        ),
        widget.Clock(
            format=' %a %d/%m/%Y %H:%M',
            background=colors["blue"],
            foreground=colors["white"],
        ),
]


##################################################################
#                           SCREENS                              #
##################################################################
from Xlib import display as xdisplay

def get_n_monitors():
    n_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output,
                                                     resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred

            if preferred:
                n_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return n_monitors


n_monitors = get_n_monitors()

screens = [
    Screen(top=bar.Bar(widgets=init_primary_widget_list(), size=25)),
]

for _ in range(n_monitors-1):
    screens.append(
        Screen(top=bar.Bar(widgets=init_secondary_widget_list(), size=25))
    )


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
