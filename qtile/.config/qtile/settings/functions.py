import psutil
from libqtile.lazy import lazy
from libqtile.backend.base import Window
from libqtile.log_utils import logger


def check_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False


@lazy.function
def window_to_prev_group(qtile):
    if qtile.current_window is None:
        return

    i = qtile.groups.index(qtile.current_group)
    prev_i = i - 1 if i > 0 else len(qtile.groups) - 1
    qtile.current_window.togroup(qtile.groups[prev_i].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.current_window is None:
        return

    i = qtile.groups.index(qtile.current_group)
    next_i = (i + 1) % len(qtile.groups)
    qtile.current_window.togroup(qtile.groups[next_i].name)


@lazy.function
def window_to_prev_screen(qtile):
    screen_idx = qtile.current_screen.index
    prev_screen_idx = screen_idx - 1 if screen_idx > 0 else len(qtile.screens) - 1
    prev_screen = qtile.screens[prev_screen_idx]
    qtile.current_window.togroup(prev_screen.group.name)


@lazy.function
def window_to_next_screen(qtile):
    screen_idx = qtile.current_screen.index
    next_screen_idx = (screen_idx + 1) % len(qtile.screens)
    next_screen = qtile.screens[next_screen_idx]
    qtile.current_window.togroup(next_screen.group.name)


@lazy.function
def toggle_layout(qtile, layout_name):
    """Try to set a layout, if it's already set, back to default"""
    DEFAULT = "monadtall"
    screen_rect = qtile.current_group.screen.get_rect()
    qtile.current_group.layout.hide()
    if qtile.current_group.layout.name == layout_name:
        qtile.current_group.cmd_setlayout(DEFAULT)
    else:
        qtile.current_group.cmd_setlayout(layout_name)
    qtile.current_group.layout.show(screen_rect)


@lazy.function
def swap_groups_between_two_screen(qtile):
    """Swap two groups between two screens"""
    if len(qtile.screens) != 2:
        return

    curr_screen_idx = qtile.current_screen.index
    other_screen_idx = 1 - curr_screen_idx
    qtile.screens[other_screen_idx].group.cmd_toscreen()


def match(window, wm_class, wm_instance):
    instance, class_ = window.get_wm_class()
    match_class = (class_ == wm_class) if wm_class else True
    match_instance = (instance == wm_instance) if wm_instance else True
    return match_class and match_instance


def find_window(qtile, wm_class, wm_instance):
    """Find existing window by WM_CLASS"""
    for window in qtile.windows_map.values():
        if not isinstance(window, Window):
            continue
        if match(window, wm_class, wm_instance):
            return window
    return None


@lazy.function
def run_or_raise(qtile, app, wm_class=None, wm_instance=None):
    """Check if the app is already launched is already running, if so focus it"""

    if not wm_class and not wm_instance:
        wm_class = app

    window = find_window(qtile, wm_class, wm_instance)

    if not window:
        qtile.cmd_spawn(app)
    else:
        window.group.cmd_toscreen()
        qtile.current_group.focus(window)

    if window == qtile.current_window:
        try:
            qtile.current_layout.cmd_swap_main()
        except AttributeError:
            return
