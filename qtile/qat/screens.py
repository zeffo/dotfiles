from typing import Any
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from qat.settings import palette

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    background=palette["base"],
)
extension_defaults = widget_defaults.copy()

class Shapes:
    left_arrow = ""
    left_semicircle = "\u25D6"

def SEP_SHAPE(bg: str, fg: str) -> list[Any]:
    return [
        widget.TextBox( # type: ignore
            text=" ",
            background=bg,
            foreground=fg
        ), 
        widget.TextBox(  # type: ignore
            text=Shapes.left_arrow, 
            background=bg,
            foreground=fg,
            padding=-15,
            fontsize=100,
        )
    ]


screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/main.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(  # type: ignore
                    highlight_method="text",
                    highlight_color=[palette["mantle"], palette["mantle"]],
                    background=palette["mantle"],
                    this_current_screen_border=palette["pink"],
                    this_screen_border=palette["pink"],
                    other_current_screen_border=palette["sky"],
                    other_screen_border=palette['sky'],
                    active=palette["sky"],
                    margin_y=3,
                    fontsize=18
                ),
                widget.AGroupBox(   # type: ignore
                    background=palette["mantle"],
                    foreground=palette["pink"],
                    border=palette["mantle"],
                    borderwidth=8,
                    margin=3
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
                    foreground=palette["pink"],
                    empty_group_string="meow UwU",
                    width=350,
                ),
                widget.Prompt(  # type: ignore
                    prompt="Run:",
                    foreground=palette["pink"],
                    background=palette["base"],
                ),
                widget.Spacer(background=palette["base"]),  # type: ignore
                *SEP_SHAPE(palette["base"], palette["pink"]),
                widget.CurrentLayoutIcon(  # type: ignore
                    background=palette["pink"],
                    foreground=palette['crust'],
                    padding=0,
                    scale=0.5,
                ),
                widget.CurrentLayout(  # type: ignore
                    background=palette["pink"],
                    foreground=palette['crust']
                ),
                *SEP_SHAPE(palette["pink"], palette["sky"]),
                widget.CPU( # type: ignore
                    background=palette['sky'],
                    foreground=palette['crust'],
                    format="{freq_current}GHz {load_percent}%"
                ),
                *SEP_SHAPE(palette["sky"], palette["pink"]),
                widget.Memory( # type: ignore
                    format="{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}",
                    measure_mem="G",
                    background=palette['pink'],
                    foreground=palette["crust"]
                ),
                *SEP_SHAPE(palette["pink"], palette["sky"]),
                widget.PulseVolume( # type: ignore
                    background=palette["sky"],
                    foreground=palette["crust"],
                    fmt='墳 {}',
                    mouse_callbacks={"Button1": lazy.spawn("pavucontrol")}
                ),
                *SEP_SHAPE(palette["sky"], palette["pink"]),
                widget.Bluetooth(   # type: ignore
                    background=palette["pink"],
                    foreground=palette["crust"],
                    hci="/dev_38_F3_2E_DD_C0_B7",
                    fmt="🎧 {}",
                    mouse_callbacks={"Button1": lazy.spawn("blueman-applet")}
                ),
                *SEP_SHAPE(palette["pink"], palette["sky"]),
                widget.Clock(   # type: ignore
                    background=palette["sky"],
                    foreground=palette["crust"],
                    format='◷ %I:%M %p',
                ),
                *SEP_SHAPE(palette["sky"], palette["pink"]),
                widget.Systray(   # type: ignore
                    background=palette["pink"],
                    foreground=palette["crust"],
                ),
                *SEP_SHAPE(palette["pink"], palette["sky"]),
                widget.Battery( # type: ignore
                    background=palette["sky"],
                    foreground=palette["crust"],
                    format="{char} {percent:2.0%}",
                    empty_char="✕",
                    charge_char="🗲",
                    discharge_char="",
                    full_char="✔️",
                    update_interval=1
                ),
                *SEP_SHAPE(palette["sky"], palette["pink"]),
                widget.QuickExit(   # type: ignore
                    background=palette["pink"],
                    foreground=palette["crust"],
                    default_text="⏻   ",
                    countdown_format="{}s",
                    # padding=8
                ),
                # *SEP_SHAPE(palette["sky"], palette["sky"])   
            ],
            39,
            margin=[9, 9, 9, 9],
			background="#00000000",
        )
    ),
    '''
        Screen(
        top=bar.Bar(
            [
                widget.GroupBox(  # type: ignore
                    highlight_method="line",
                    highlight_color=[palette["mantle"], palette["mantle"]],
                    background=palette["mantle"],
                    this_current_screen_border=palette["sky"],
                    this_screen_border=palette["sky"],
                    other_current_screen_border=palette["pink"],
                    other_screen_border=palette['pink'],
                    active=palette["sky"],
                    margin_y=5
                ),
                widget.AGroupBox(   # type: ignore
                    background=palette["mantle"],
                    foreground=palette["sky"],
                    border=palette["mantle"],
                    borderwidth=8,
                    margin=3
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
                    foreground=palette["sky"],
                    empty_group_string="meow UwU",
                    width=800,
                ),
                widget.TextBox(  # type: ignore
                    text="\uE0B0",
                    background=palette["crust"],
                    foreground=palette["base"],
                    padding=0,
                    fontsize=35,
                ),
            ],
            39,
            margin=[9, 9, 9, 9],
            background=palette["crust"]
        )
    )
    '''
]

