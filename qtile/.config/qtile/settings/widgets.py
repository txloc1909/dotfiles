from libqtile import widget

# _FONT = "Ubuntu Mono"
_FONT = "Source Code Pro for Powerline"
_FONT_SIZE = 14
_WIDGET_PADDING = 3

_WIFI_INTERFACE = "wlx14ebb6474923"


def init_widget_default():
    return {
        "font": _FONT,
        "fontsize": _FONT_SIZE,
        "padding": _WIDGET_PADDING,
    }


def primary_widgets():
    return [
        widget.GroupBox(),
        widget.Sep(),
        widget.CurrentLayoutIcon(scale=0.75),
        widget.CurrentLayout(),
        widget.Sep(),
        widget.WindowName(),
        widget.CurrentScreen(),
        widget.Sep(),
        widget.CPU(format="CPU: {load_percent:2}%"),
        widget.Sep(),
        widget.Memory(format="MEM: {MemUsed:2.3f}GB", measure_mem="G"),
        widget.Sep(),
        widget.Net(interface=_WIFI_INTERFACE, format=" {down} ↓↑ {up} "),
        widget.Sep(),
        widget.Wlan(interface=_WIFI_INTERFACE, format="{essid}"),
        widget.Sep(),
        widget.Battery(format="BAT: {percent:2.0%}"),
        widget.Sep(),
        widget.Clock(format="%Y-%m-%d %a %H:%M"),
        widget.Systray(),
    ]


def secondary_widgets():
    return [
        widget.GroupBox(),
        widget.Sep(),
        widget.CurrentLayoutIcon(scale=0.75),
        widget.CurrentLayout(),
        widget.Sep(),
        widget.WindowName(),
        widget.CurrentScreen(),
        widget.Sep(),
        widget.Battery(format="BAT: {percent:2.0%}"),
        widget.Sep(),
        widget.Clock(format="%Y-%m-%d %a %H:%M"),
    ]
