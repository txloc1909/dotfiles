import os
import subprocess

from libqtile import hook, qtile

from settings.keys import init_spawning_keys, init_common_keys, init_layout_keys
from settings.groups import init_groups, init_group_keys
from settings.widgets import init_widget_default
from settings.screens import init_screens
from settings.layouts import init_layouts, init_floating_layout
from settings.mouse import init_mouse
from settings.functions import check_process_running


keys = []
keys.extend(init_common_keys())
keys.extend(init_layout_keys())
keys.extend(init_spawning_keys())

groups = init_groups()
keys.extend(init_group_keys())

layouts = init_layouts()

widget_defaults = init_widget_default()
extension_defaults = widget_defaults.copy()

screens = init_screens()

mouse = init_mouse()

floating_layout = init_floating_layout()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = "floating_only"
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    startup_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([startup_script])


@hook.subscribe.client_name_updated
def move_spotify(client):
    """Move Spotify client to correct group since its wm_class setting is slow"""
    MUSIC_GROUP = "8"
    if client.cmd_info().get("name") == "Spotify" and not client.get_wm_class():
        client.cmd_togroup(MUSIC_GROUP)


@hook.subscribe.client_new
def fullscreen_off(client):
    """Toggle fullscreen off in case there is any fullscreen window in group"""
    try:
        group = client.group
    except AttributeError:
        return

    if not group:
        assert qtile is not None, "this should never happen"
        group = qtile.current_group

    for win in group.windows:
        if win.fullscreen:
            win.toggle_fullscreen()


wmname = "LG3D"
