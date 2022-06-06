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
        active="ffffff",
        inactive="404040",
        highlight_method="line",
        urgent_alert_method="block",
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
    return widget.Memory(format=" {MemUsed:2.3f}GB", measure_mem="G")


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


def primary_widgets():
    return [
        current_screen(),
        right_arrow(),
        groupbox(),
        right_arrow(),
        *current_layout(),
        right_arrow(),
        window_title(),
        left_arrow(),
        cpu(),
        left_arrow(),
        ram(),
        left_arrow(),
        net_speed(),
        left_arrow(),
        wifi_ssid(),
        left_arrow(),
        volume(),
        left_arrow(),
        *battery(),
        left_arrow(),
        datetime(),
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
        window_title(),
        left_arrow(),
        *battery(),
        left_arrow(),
        datetime(),
    ]
