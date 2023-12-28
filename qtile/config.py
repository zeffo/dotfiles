from libqtile import hook
from pathlib import Path
import subprocess
from core import *


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once  # type: ignore (no stubs)
def autostart():
    script = Path.home() / Path(".config/qtile/autostart.sh")
    subprocess.Popen([script])
