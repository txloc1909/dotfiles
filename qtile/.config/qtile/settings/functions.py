import psutil


def check_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False


def window_to_prev_group(qtile):
    if qtile.current_window is None:
        return

    i = qtile.groups.index(qtile.current_group)
    prev_i = i - 1 if i > 0 else len(qtile.groups) - 1
    qtile.current_window.togroup(qtile.groups[prev_i].name)


def window_to_next_group(qtile):
    if qtile.current_window is None:
        return

    i = qtile.groups.index(qtile.current_group)
    next_i = (i + 1) % len(qtile.groups)
    qtile.current_window.togroup(qtile.groups[next_i].name)


def window_to_prev_screen(qtile):
    screen_idx = qtile.current_screen.index
    prev_screen_idx = screen_idx - 1 if screen_idx > 0 else len(qtile.screens) - 1
    prev_screen = qtile.screens[prev_screen_idx]
    qtile.current_window.togroup(prev_screen.group.name)


def window_to_next_screen(qtile):
    screen_idx = qtile.current_screen.index
    next_screen_idx = (screen_idx + 1) % len(qtile.screens)
    next_screen = qtile.screens[next_screen_idx]
    qtile.current_window.togroup(next_screen.group.name)
