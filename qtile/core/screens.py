from catppuccin import Colour
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from itertools import cycle
from .settings import palette

widget_defaults = dict(
    font="SpaceMono Nerd Font Mono",
    fontsize=15,
    background=palette.base.hex,
)
extension_defaults = widget_defaults.copy()


class Builder:
    def __init__(self):
        self.bar = []
        self.colors = cycle(
            [
                palette.pink,
                palette.mauve,
                palette.red,
                palette.peach,
                palette.yellow,
                palette.green,
                palette.teal,
                palette.sapphire,
                palette.blue,
                palette.lavender,
            ]
        )
        self._prev = None

    def _add_widget(self, widget):
        self.bar.append(widget)

    def add_widget(self, widget, *, append_divider: bool = True):
        color: Colour = self._prev or next(self.colors)
        widget.background = color.hex
        widget.foreground = palette.base.hex

        self.bar.append(widget)

        if append_divider:
            next_color = next(self.colors)
            self._prev = next_color
            self.bar.extend(self.get_divider(color, next_color))

    def get_divider(self, bg: Colour, fg: Colour):
        return [
            widget.TextBox(text="  ", background=bg.hex, foreground=fg.hex),  # type: ignore
            widget.TextBox(  # type: ignore
                text="◀",
                background=bg.hex,
                foreground=fg.hex,
                padding=-15,
                fontsize=80,
            ),
        ]


bar0 = Builder()

bar0._add_widget(
    widget.GroupBox(  # type: ignore
        highlight_method="line",
        highlight_color=[palette.mantle.hex, palette.mantle.hex],
        margin_y=3,
        fontsize=18,
        active=palette.pink.hex,
        inactive=palette.base.hex,
        other_current_screen_border=palette.red.hex,
        other_screen_border=palette.red.hex,
        this_current_screen_border=palette.mauve.hex,
        this_screen_border=palette.mauve.hex,
        background=palette.mantle.hex,
    )
)
bar0._add_widget(
    widget.AGroupBox(
        background=palette.mantle.hex,
        foreground=palette.pink.hex,
        border=palette.mantle.hex,
        borderwidth=8,
        margin=3,
    )
)
bar0._add_widget(
    widget.TextBox(  # type: ignore
        text="\uE0B0",
        foreground=palette.mantle.hex,
        background=palette.base.hex,
        padding=0,
        fontsize=35,
    )
)
bar0._add_widget(
    widget.WindowName(  # type: ignore
        background=palette.base.hex,
        format="{name}",
        foreground=palette.pink.hex,
        empty_group_string="<3",
        width=350,
    )
)

bar0._add_widget(
    widget.Prompt(  # type: ignore
        prompt="Run:",
        foreground=palette.pink.hex,
        background=palette.base.hex,
    )
)

bar0._add_widget(widget.Spacer(background=palette.base.hex))
bar0.bar.extend(bar0.get_divider(palette.base, palette.pink))
bar0.add_widget(widget.CurrentLayoutIcon(padding=0, scale=0.5))
bar0.add_widget(widget.CurrentLayout())
bar0.add_widget(widget.CPU(format="{freq_current}GHz {load_percent}%"))
bar0.add_widget(widget.ThermalSensor(format="CPU {temp:.0f}{unit}"))
bar0.add_widget(
    widget.Memory(
        format="RAM {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
        measure_mem="G",
    )
)
bar0.add_widget(
    widget.PulseVolume(
        limit_max_volume=True,
        update_interval=0.02,
        get_volume_command="pamixer --get-volume",
        fmt="🎶 {}",
        mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
    )
)

bar0.add_widget(
    widget.Bluetooth(
        hci="/dev_38_F3_2E_DD_C0_B7",
        fmt="🎧 {}",
        mouse_callbacks={"Button1": lazy.spawn("blueman-applet")},
    )
)

bar0.add_widget(widget.Clock(format="◷ %I:%M %p"))
bar0.add_widget(widget.Systray())
bar0.add_widget(widget.QuickExit(default_text="⏻  ", fontsize=22), append_divider=False)

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/main.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            bar0.bar,
            42,
            margin=[9, 9, 9, 9],
            background="#FFFFFF",
            border_width=[1, 0, 1, 0],
            border_color=palette.base.hex,
        ),
    ),
    Screen(
        wallpaper="~/.config/qtile/wallpapers/main.png",
        wallpaper_mode="fill",
    ),
]
