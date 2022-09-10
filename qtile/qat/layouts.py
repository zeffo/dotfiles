from libqtile.layout import MonadThreeCol, Tile, Matrix, Floating
from libqtile.config import Match

from qat.settings import palette


settings = {"margin": 20, "border_focus": palette["pink"]}

layouts = [MonadThreeCol(**settings), Tile(**settings), Matrix(**settings), Floating()]

floating_layout = Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
