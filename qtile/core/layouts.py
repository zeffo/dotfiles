from libqtile.layout import xmonad, tile, matrix, floating, columns
from libqtile.config import Match

from .settings import palette


settings = {
    "margin": 20,
    "border_width": 2,
    "border_focus": palette.pink.hex,
    "border_normal": palette.base.hex,
}

layouts = [
    tile.Tile(**settings, add_on_top=False, add_after_last_=True),
    xmonad.MonadThreeCol(**settings),
    matrix.Matrix(**settings),
    columns.Columns(**settings),
]

floating_layout = floating.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *floating.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=0,
)
