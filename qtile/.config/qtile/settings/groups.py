from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import mod, alt
from .functions import swap_groups_between_two_screen


_group_names = list("123456789")

_group_rules = {
    "1": [Match(wm_class="firefox")],
    "2": [
        Match(wm_class="local-tmux"),
        Match(wm_class="Gnome-terminal"),
    ],
    "3": [Match(wm_class="notion-snap", wm_instance_class="notion-snap")],
    "4": [Match(wm_class="obsidian", wm_instance_class="obsidian")],
    "6": [Match(wm_class="Virt-manager", wm_instance_class="virt-manager")],
    "7": [
        Match(wm_class="Skype", wm_instance_class="skype"),
        Match(wm_class="discord", wm_instance_class="discord"),
        Match(wm_class="Slack", wm_instance_class="slack"),
    ],
    "8": [
        Match(wm_class="Spotify", wm_instance_class="spotify"),
        Match(wm_class="Brave-browser", wm_instance_class="youtube.com"),
    ],
    "9": [
        Match(wm_class="Brave-browser"),
        Match(wm_class="Ferdi", wm_instance_class="ferdi"),
    ],
}

_default_layout = {
    "1": "monadtall",
    "2": "max",
    "3": "monadtall",
    "4": "max",
    "5": "monadtall",
    "6": "max",
    "7": "max",
    "8": "max",
    "9": "monadtall",
}


def init_groups():
    return [
        Group(
            i,
            matches=_group_rules.get(i, None),
            layout=_default_layout.get(i, None),
        )
        for i in _group_names
    ]


def init_group_keys():
    keys = []
    for i in _group_names:
        keys.extend(
            [
                Key([alt, "control"], i, lazy.group[i].toscreen()),
                Key([mod], i, lazy.group[i].toscreen()),
                Key([mod, "shift"], i, lazy.window.togroup(i, switch_group=True)),
            ]
        )

    keys.append(Key([mod], "0", swap_groups_between_two_screen))
    keys.append(Key([alt, "control"], "0", swap_groups_between_two_screen))
    return keys
