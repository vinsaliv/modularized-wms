# File: config.py
import os
from modules.groups import groups
from modules.hooks import *
from modules.keys import mod, keys
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import widget_defaults, extension_defaults, screens

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"