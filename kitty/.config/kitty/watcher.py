from typing import Any, Dict

from kitty.boss import Boss
from kitty.window import Window 
from kitty.fast_data_types import viewport_for_window


def _is_too_small(cols, lines):
    return cols < 110 and lines < 30


def _is_too_narrow(cols):
    return cols < 120


def _get_layout_name_only(layout):
    return layout.split(":")[0]


def on_resize(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    _, _, vp_w, vp_h, cell_w, cell_h = viewport_for_window(window.os_window_id)
    columns, lines = vp_w // cell_w, vp_h // cell_h

    if _is_too_small(columns, lines):
        new_layout = "stack"
    elif _is_too_narrow(columns):
        new_layout = "vertical"
    else:
        new_layout = "tall:bias=55"
    
    tab = window.tabref()
    if not tab:
        return 

    curr_layout = tab.current_layout.name
    if _get_layout_name_only(new_layout) != _get_layout_name_only(curr_layout):
        tab.goto_layout(new_layout)

    # # Debug
    # with open("~/.cache/kitty.log", "a") as f:
    #     f.write(f"{window.os_window_id}: {columns}, {lines}; {curr_layout=} -> {new_layout=}\n")
