# File: mouse.py
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click(
        [mod],
        "Button2",
        lazy.window.bring_to_front()
    ),
]