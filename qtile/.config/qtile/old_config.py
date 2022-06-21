import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

import arcobattery  # battery widget from ArcoLinux


##################################################################
#                             VARIABLES                          #
##################################################################

mod = "mod4"  # Super/Window key
alt = "mod1"  # Alt key
terminal = os.environ.get("TERMINAL", None) or "alacritty"
run_launcher = "rofi -modi run,drun -show drun"
dmenu_launcher = "dmenu_run"
web_browser = os.environ.get("BROWSER", None) or "firefox"
file_manager = "nemo"
home = os.path.expanduser("~")  # home directory

# Color scheme
monokai = {
    "background": "272822",  # black/grey-ish
    "foreground": "f8f8f2",  # white & yellow-ish
    "comment": "75715e",  # grey & yellow-ish
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
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),  # in COLUMNS layout
        lazy.layout.swap_left(),  # in MONADTALL layout
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left().when(layout="columns"),  # in COLUMNS layout
        lazy.layout.shrink().when(layout="monadtall"),  # in MONADTALL layout
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right().when(layout="columns"),
        lazy.layout.grow().when(layout="monadtall"),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    Key([alt], "Tab", lazy.screen.toggle_group()),
    Key([mod], "q", lazy.window.kill()),
    # Qtile restart/quiting
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "c", lazy.reload_config()),
    Key([mod], "b", lazy.hide_show_bar()),
    # Multi monitors operation
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    # Spawn programs
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "r", lazy.spawn(run_launcher)),
    Key([mod], "d", lazy.spawn(dmenu_launcher)),
    Key([mod], "w", lazy.spawn(web_browser)),
    Key([mod], "e", lazy.spawn(file_manager)),
    Key([mod], "y", lazy.spawn("youtube")),
    Key([mod], "g", lazy.spawn("searchweb")),
    # Move visually between groups
    Key([mod, alt], "h", lazy.screen.prev_group()),
    Key([mod, alt], "l", lazy.screen.next_group()),
    # Directly switch to layout
    Key([mod], "t", lazy.group.setlayout("tile")),
    Key([mod], "m", lazy.group.setlayout("max")),
    Key([mod, "shift"], "t", lazy.group.setlayout("columns")),
    Key([mod, "shift"], "f", lazy.group.setlayout("floating")),
    Key([mod], "i", lazy.group.focus_back()),
]

##################################################################
#                            GROUPS                              #
##################################################################


def toscreen(qtile, group_name):
    """Switch to a specific group,
    and if already at that group, go back to previous group
    Similar to i3wm's workspace back_and_forth option
    """
    if group_name == qtile.current_screen.group.name:
        return qtile.current_screen.set_group(qtile.current_screen.previous_group)
    for i, group in enumerate(qtile.groups):
        if group_name == group.name:
            return qtile.current_screen.set_group(qtile.groups[i])


groups = [Group(i, layout="tile") for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group's number = switch to group
            Key(
                [mod],
                i.name[0],
                # lazy.group[i.name].toscreen(),
                lazy.function(toscreen, i.name),
            ),
            # mod1 + shift + group's number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name[0],
                lazy.window.togroup(i.name, switch_group=True),
            ),
        ]
    )

##################################################################
#                           LAYOUTS                              #
##################################################################

# Default theme for layouts
layout_theme = {
    "border_width": 4,
    "margin": 6,
    "border_focus": colors["green"],
    "border_normal": colors["black"],
}

layouts = [
    layout.MonadTall(new_client_position="top", **layout_theme),
    layout.Columns(
        border_focus_stack=monokai["green"],
        border_normal_stack=monokai["background"],
        insert_position=1,
        **layout_theme
    ),
    layout.Tile(
        border_on_single=True,
        margin_on_single=False,
        ratio=0.55,
        ratio_increment=0.05,
        **layout_theme
    ),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

##################################################################
#                              BARS                              #
##################################################################

# Default theme for widgets & extensions
widget_defaults = dict(
    # font='Ubuntu Mono',
    # font="MesloLGS NF",
    font="Source Code Pro for Powerline",
    fontsize=14,
    padding=3,
    background=monokai["background"],
)
extension_defaults = widget_defaults.copy()


def init_primary_widget_list():
    return [
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
        widget.WindowName(
            padding=10,
            # for_current_screen=True,
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
            interface="wlx14ebb6474923",
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
        # widget.BatteryIcon(),
        arcobattery.BatteryIcon(
            padding=0,
            scale=0.7,
            y_poss=2,
            theme_path=os.path.expanduser("~/.config/qtile/battery_icons_horiz"),
            update_interval=5,
            background=monokai["green"],
        ),
        widget.Battery(
            # format="  {percent:2.0%} ",
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
            format=" %a %d/%m/%Y %H:%M",
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
        widget.WindowName(
            padding=10,
            # for_current_screen=True,
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
            interface="wlx14ebb6474923",
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
            theme_path=os.path.expanduser("~/.config/qtile/battery_icons_horiz"),
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
            format=" %a %d/%m/%Y %H:%M",
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
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
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

for _ in range(n_monitors - 1):
    screens.append(Screen(top=bar.Bar(widgets=init_secondary_widget_list(), size=25)))


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# Execute autostart script once login
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    startup_script = home + "/.config/qtile/autostart.sh"
    subprocess.call([startup_script])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
