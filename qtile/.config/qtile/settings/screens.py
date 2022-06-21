from libqtile.config import Screen
from libqtile import bar
from Xlib import display as xdisplay

from .widgets import primary_widgets, secondary_widgets, bottom_widgets

_BAR_HEIGHT = 24


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
    except Exception:
        # always setup at least one monitor
        return 1
    else:
        return n_monitors


def init_bar(widgets):
    return bar.Bar(widgets=widgets, size=_BAR_HEIGHT)


def init_screens():
    num_screens = get_n_monitors()
    screens = [
        Screen(
            top=init_bar(widgets=primary_widgets()),
            bottom=init_bar(widgets=bottom_widgets()),
        )
    ]
    for _ in range(num_screens - 1):
        screens.append(Screen(top=init_bar(widgets=secondary_widgets())))

    return screens
