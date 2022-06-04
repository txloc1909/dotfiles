from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .keys import mod


group_names = list("123456789")


def init_groups():
    return [Group(i) for i in group_names]


def init_group_keys():
    keys = []
    for i in group_names:
        keys.extend(
            [
                Key([mod], i, lazy.group[i].toscreen()),
                Key([mod, "shift"], i, lazy.window.togroup(i, switch_group=True)),
            ]
        )

    return keys
