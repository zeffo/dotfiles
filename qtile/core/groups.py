from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .keys import keys
from .settings import mod

layout = "tile"
workspaces: list[str | Group] = ["HOME", "WEB", "DEV", "DSC", "SPT", "SYS"]

groups: list[Group] = []

symbol = "⬤"

for i, ws in enumerate(workspaces):
    if isinstance(ws, str):
        ws = Group(ws, layout=layout, label=symbol)

    groups.append(ws)

    i = str(i + 1)
    keys.extend(
        [
            Key(
                [mod],
                i,
                lazy.group[ws.name].toscreen(),
                desc="Switch to group {}".format(ws.name),
            ),
            Key(
                [mod, "shift"],
                i,
                lazy.window.togroup(
                    ws.name, switch_group=False
                ),  # set switch_group to True to switch and move
                desc="Switch to & move focused window to group {}".format(ws.name),
            ),
        ]
    )
