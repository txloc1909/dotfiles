import os
from collections import defaultdict

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from .functions import window_to_prev_group, window_to_next_group
from .functions import window_to_prev_screen, window_to_next_screen
from .functions import toggle_layout
from .functions import run_or_raise

mod = "mod4"
alt = "mod1"
terminal = os.environ.get("TERMINAL", guess_terminal())
browser = os.environ.get("BROWSER", "firefox")
sec_browser = "brave-browser"
local_tmux_cmd = "alacritty --class alacritty,local-tmux -e launch-local-tmux"


def init_spawning_keys():
    return [
        Key(
            [mod, "shift"],
            "Return",
            run_or_raise(local_tmux_cmd, wm_instance="local-tmux"),
        ),
        Key([mod], "Return", lazy.spawn(terminal)),
        Key([mod], "s", lazy.spawn("rofi -show ssh")),
        Key([mod], "w", run_or_raise(browser)),
        Key([mod], "e", run_or_raise(sec_browser, wm_instance=sec_browser)),
        Key([mod], "y", run_or_raise("youtube", wm_instance="youtube.com")),
        Key([mod], "r", lazy.spawn("rofi -show drun -monitor -1")),
        Key([mod], "d", lazy.spawn("dmenu_run")),
        Key([mod], "g", lazy.spawn("searchweb")),
        Key([mod, alt], "l", lazy.spawn("i3lock-fancy")),
        Key([alt, "control"], "u", run_or_raise(browser)),
        Key(
            [alt, "control"],
            "i",
            run_or_raise(local_tmux_cmd, wm_instance="local-tmux"),
        ),
        Key(
            [alt, "control"],
            "e",
            run_or_raise("brave-browser", wm_instance="brave-browser"),
        ),
        Key([alt, "control"], "n", run_or_raise("obsidian")),
        Key([alt, "control"], "y", run_or_raise("youtube", wm_instance="youtube.com")),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
        Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle")),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
        Key([], "F12", lazy.spawn("todolist")),
    ]


def layout_keys():
    return {
        "monadtall": {
            ((mod,), "j"): lazy.layout.down,
            ((mod,), "k"): lazy.layout.up,
            ((mod,), "h"): lazy.layout.shrink_main,
            ((mod,), "l"): lazy.layout.grow_main,
            ((mod,), "u"): lazy.layout.zoom,
            ((mod,), "i"): lazy.layout.switch_col,
            ((mod, "shift"), "j"): lazy.layout.shuffle_down,
            ((mod, "shift"), "k"): lazy.layout.shuffle_up,
            ((mod, "shift"), "h"): lazy.layout.shrink,
            ((mod, "shift"), "l"): lazy.layout.grow,
            ((mod, "shift"), "o"): lazy.layout.normalize,
        },
        "columns": {
            ((mod,), "j"): lazy.layout.down,
            ((mod,), "k"): lazy.layout.up,
            ((mod,), "h"): lazy.layout.left,
            ((mod,), "l"): lazy.layout.right,
            ((mod,), "u"): lazy.layout.toggle_split,
            ((mod,), "i"): lazy.layout.switch_col,
            ((mod, "shift"), "j"): lazy.layout.shuffle_down,
            ((mod, "shift"), "k"): lazy.layout.shuffle_up,
            ((mod, "shift"), "h"): lazy.layout.shuffle_left,
            ((mod, "shift"), "l"): lazy.layout.shuffle_right,
            ((mod, "control"), "j"): lazy.layout.grow_down,
            ((mod, "control"), "k"): lazy.layout.grow_up,
            ((mod, "control"), "h"): lazy.layout.grow_left,
            ((mod, "control"), "l"): lazy.layout.grow_right,
            ((mod, "shift"), "o"): lazy.layout.normalize,
        },
        "max": {
            ((mod,), "j"): lazy.layout.next,
            ((mod,), "k"): lazy.layout.previous,
        },
    }


def init_layout_keys():
    join_keys = defaultdict(list)
    for layout, keybinds in layout_keys().items():
        for keybind, func in keybinds.items():
            join_keys[keybind].append((func, layout))

    keys = []
    for (mods, key), binds in join_keys.items():
        bind_list = [func().when(layout=layout) for func, layout in binds]
        keys.append(Key(list(mods), key, *bind_list))

    return keys


def init_common_keys():
    return [
        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod, "shift"], "space", lazy.window.toggle_floating()),
        Key([mod], "Tab", lazy.next_layout()),
        Key([alt], "Tab", lazy.group.focus_back()),
        Key([alt], "space", lazy.screen.toggle_group()),
        Key([mod], "q", lazy.window.kill()),
        Key([alt, "control"], "j", lazy.layout.next()),
        Key([alt, "control"], "k", lazy.layout.previous()),
        Key([alt, "control"], "f", lazy.window.toggle_fullscreen()),
        Key([alt, "control"], "m", lazy.window.toggle_maximize()),
        Key([mod, "shift"], "c", lazy.reload_config()),
        Key([mod, "shift"], "r", lazy.restart()),
        Key([mod, "shift"], "q", lazy.shutdown()),
        Key([mod], "b", lazy.hide_show_bar()),
        Key([mod], "period", lazy.next_screen()),
        Key([mod], "comma", lazy.prev_screen()),
        Key([mod, "shift"], "period", window_to_prev_screen),
        Key([mod, "shift"], "comma", window_to_next_screen),
        Key([mod], "t", toggle_layout("monadtall")),
        Key([mod], "m", toggle_layout("max")),
        Key([mod], "c", toggle_layout("columns")),
        Key([mod, "control"], "Left", window_to_prev_group),
        Key([mod, "control"], "Right", window_to_next_group),
    ]
