from libqtile import bar, widget
from libqtile.config import Screen

from qat.settings import palette

widget_defaults = dict(
    fontsize=18,
    background=palette["base"],
    foreground=palette["teal"],
    padding=10,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(  # type: ignore
                    highlight_method="text",
                    this_current_screen_border=palette["teal"],
                    active=palette["lavender"],
                    background=palette["mantle"],
                ),
                widget.TextBox(  # type: ignore
                    text="\uE0B0",
                    foreground=palette["mantle"],
                    background=palette["base"],
                    padding=0,
                    fontsize=35,
                ),
                widget.WindowName(  # type: ignore
                    background=palette["base"],
                    format="{name}",
                    foreground=palette["teal"],
                    empty_group_string="Desktop",
                    width=320,
                ),
                widget.TextBox(  # type: ignore
                    text="\uE0B0",
                    background=palette["teal"],
                    foreground=palette["base"],
                    padding=0,
                    fontsize=35,
                ),
                widget.Net(  # type: ignore
                    background=palette["teal"],
                    foreground=palette["crust"],
                    format="{down} ↓↑ {up}",
                ),
                widget.TextBox(  # type: ignore
                    text="\uE0B0",
                    background=palette["base"],
                    foreground=palette["teal"],
                    padding=0,
                    fontsize=35,
                ),
                widget.Prompt(  # type: ignore
                    prompt="Run:",
                    foreground=palette["teal"],
                    background=palette["base"],
                ),
                widget.Spacer(background=palette["base"]),  # type: ignore
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["base"],
                    foreground=palette["blue"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.CurrentLayoutIcon(  # type: ignore
                    background=palette["blue"],
                    padding=0,
                    scale=0.5,
                ),
                widget.CurrentLayout(  # type: ignore
                    background=palette["blue"],
                ),
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["blue"],
                    foreground=palette["pink"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.CPU(  # type: ignore
                    background=palette["pink"], format="  {load_percent}%"
                ),
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["pink"],
                    foreground=palette["peach"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.Memory(  # type: ignore
                    background=palette["peach"],
                    format="  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
                    measure_mem="G",
                ),
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["peach"],
                    foreground=palette["green"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.TextBox(  # type: ignore
                    text="墳 ",
                    background=palette["green"],
                    padding=0,
                ),
                widget.PulseVolume(  # type: ignore
                    background=palette["green"],
                ),
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["green"],
                    foreground=palette["mauve"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.Clock(  # type: ignore
                    format="  %I:%M %p",
                    background=palette["mauve"],
                ),
                widget.TextBox(  # type: ignore
                    text="",
                    background=palette["mauve"],
                    foreground=palette["base"],
                    padding=-17,
                    fontsize=108,
                ),
                widget.Systray(  # type: ignore
                    icon_size=30, background=palette["base"]
                ),
            ],
            39,
            margin=[9, 9, 9, 9],
        ),
    ),
]
