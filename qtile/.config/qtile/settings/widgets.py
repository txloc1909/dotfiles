import os

from libqtile import widget

from .arcobattery import BatteryIcon

_FONT = "Source Code Pro for Powerline"
_FONT_SIZE = 14
_WIDGET_PADDING = 3

_WIFI_INTERFACE = "wlx14ebb6474923"

_BATTERY_ICON_DIR = os.path.expanduser("~/.config/qtile/battery_icons_horiz")


def init_widget_default():
    return {
        "font": _FONT,
        "fontsize": _FONT_SIZE,
        "padding": _WIDGET_PADDING,
        "background": "222222",
    }


def left_arrow():
    return widget.TextBox(text="")


def right_arrow():
    return widget.TextBox(text="")


def current_screen():
    return widget.CurrentScreen(
        active_text="",  # nf-fa-check_circle
        inactive_text="",  # nf-fa-check_circle_off
        fontsize=_FONT_SIZE + 2,
        padding=5,
    )


def groupbox():
    return widget.GroupBox(
        foreground="ffffff",
        active="ffffff",
        inactive="444444",
        this_current_screen_border="034685",
        this_screen_border="034685",
        other_current_screen_border="777777",
        other_screen_border="777777",
        block_highlight_text_color="ffffff",
        highlight_method="block",
        urgent_alert_method="border",
        urgent_border="ff0000",
        disable_drag=True,
    )


def current_layout():
    return [
        widget.CurrentLayoutIcon(scale=0.75),
        widget.CurrentLayout(),
    ]


def window_title():
    return widget.WindowName(padding=5)


def cpu():
    return widget.CPU(format=" {load_percent:3}%")


def ram():
    return widget.Memory(
        format=" {MemUsed:2.3f}GB ({MemPercent:2.1f}%)",
        measure_mem="G",
    )


def net_speed():
    return widget.Net(interface=_WIFI_INTERFACE, format="{up} ↑↓ {down}")


def wifi_ssid():
    return widget.Wlan(interface=_WIFI_INTERFACE, format=" {essid}")


def volume():
    return widget.Volume(fmt=" {}")


def battery():
    return [
        BatteryIcon(
            padding=0,
            scale=0.7,
            y_poss=2,
            theme_path=_BATTERY_ICON_DIR,
            update_interval=5,
        ),
        widget.Battery(
            format="{percent:2.0%}",
        ),
    ]


def datetime():
    return widget.Clock(format=" %a %e %b %Y %H:%M")


def window_count():
    return widget.WindowCount(
        text_format=" {num}",  # nf-fa-windows
        show_zero=True,
    )


def task_list():
    return widget.TaskList(
        border="034685",
        highlight_method="block",
        fontsize=_FONT_SIZE - 4,
        icon_size=_FONT_SIZE,
        margin=2,
        title_width_method="uniform",
        max_title_width=400,
        txt_floating=" ",  # nf-fa-window_restore
        txt_maximized=" ",  # nf-fa-arrows_alt
        txt_minimized=" ",  # nf-fa-window_minimize
    )


def primary_widgets():
    return [
        current_screen(),
        right_arrow(),
        groupbox(),
        right_arrow(),
        *current_layout(),
        right_arrow(),
        # window_title(),
        widget.Spacer(),
        left_arrow(),
        wifi_ssid(),
        left_arrow(),
        volume(),
        left_arrow(),
        *battery(),
        left_arrow(),
        datetime(),
        left_arrow(),
        widget.Systray(),
    ]


def secondary_widgets():
    return [
        current_screen(),
        right_arrow(),
        groupbox(),
        right_arrow(),
        *current_layout(),
        right_arrow(),
        window_count(),
        right_arrow(),
        window_title(),
        left_arrow(),
        wifi_ssid(),
        left_arrow(),
        volume(),
        left_arrow(),
        *battery(),
        left_arrow(),
        datetime(),
    ]


def bottom_widgets():
    return [
        window_count(),
        right_arrow(),
        task_list(),
        left_arrow(),
        cpu(),
        left_arrow(),
        ram(),
        left_arrow(),
        net_speed(),
    ]
