import os
import subprocess

from libqtile import hook

from settings.keys import init_sxhkd_keys, init_common_keys, init_layout_keys
from settings.groups import init_groups, init_group_keys
from settings.widgets import init_widget_default
from settings.screens import init_screens
from settings.layouts import init_layouts, init_floating_layout
from settings.mouse import init_mouse
from settings.functions import check_process_running


keys = []
keys.extend(init_common_keys())
keys.extend(init_layout_keys())
if not check_process_running("sxhkd"):
    keys.extend(init_sxhkd_keys())

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
bring_front_click = False
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


wmname = "LG3D"
