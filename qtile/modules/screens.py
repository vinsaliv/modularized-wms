# File: screens.py
from libqtile import bar, widget
from libqtile.config import Screen

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Clock(format="%I:%M %p"),
            ],
            24,
        ),
    ),
]