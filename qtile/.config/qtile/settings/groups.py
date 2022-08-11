from libqtile import hook
from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import mod


_group_names = list("123456789")

_group_rules = {
    "1": [Match(wm_class="firefox")],
    "3": [Match(wm_class="notion-snap", wm_instance_class="notion-snap")],
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
    "1": "max",
    "8": "max",
    "9": "max",
}


@hook.subscribe.client_name_updated
def move_spotify(client):
    """Move Spotify client to correct group since its wm_class setting is slow"""
    if client.cmd_info().get("name") == "Spotify" and not client.get_wm_class():
        client.cmd_togroup("8")


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
                Key([mod], i, lazy.group[i].toscreen()),
                Key([mod, "shift"], i, lazy.window.togroup(i, switch_group=True)),
            ]
        )

    return keys
