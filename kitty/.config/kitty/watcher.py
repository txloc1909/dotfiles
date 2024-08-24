from typing import Any, Dict

from kitty.boss import Boss
from kitty.window import Window 

LOG_FILE = "/home/loctx/kitty.log"


def on_resize(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    new_geometry = data.get("new_geometry")
    columns = new_geometry.xnum
    lines = new_geometry.ynum

    with open(LOG_FILE, "a") as f:
        f.write(f"{window.id}:{columns},{lines}\n")
    
    new_layout = None
    if columns < 120:
        new_layout = "vertical"
    elif columns < 120 and lines < 54:
        new_layout = "stack"

    tab = window.tabref()
    
    with open(LOG_FILE, "a") as f:
        f.write(f"{window.id}:{new_layout},{tab}\n")
