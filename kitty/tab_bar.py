# pyright: reportMissingImports=false
# pyright: reportGeneralTypeIssues=false

from kitty.fast_data_types import Color, Screen, get_options
from catppuccin import PALETTE
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    TabBarData,
    as_rgb,
    draw_tab_with_powerline,
    draw_title,
)
from kitty.utils import color_as_int
import random

opts = get_options()

flavor = PALETTE.mocha.colors
fields = (
    "pink",
    "red",
    "peach",
    "yellow",
    "green",
    "blue",
    "mauve",
)


def cai(color):
    """color as int"""
    return int(
        "".join(["{:02x}".format(x) for x in (color.r, color.g, color.b, color.a)]), 16
    )


colors = []
for field in fields:
    rgb = getattr(flavor, field).rgb
    color = Color(rgb.r, rgb.g, rgb.b, alpha=2)
    colors.append(color)


powerline_symbols = {
    "slanted": ("", "╱", ""),
    "round": ("", "", ""),
}

salt = random.randint(0, len(colors) - 1)


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_tab_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    idx = index - 1 + salt
    cur_color = colors[idx % len(colors)]
    tab_bg = cai(cur_color)
    tab_bar_background = color_as_int(opts.tab_bar_background)
    default_bg = as_rgb(int(draw_data.default_bg))
    if extra_data.next_tab:
        next_tab_bg = cai(colors[(idx + 1) % len(colors)])
    else:
        next_tab_bg = default_bg

    separator_symbol, _, back_separator_symbol = powerline_symbols.get(
        draw_data.powerline_style, ("", "", "")
    )
    min_title_length = 1 + 2
    start_draw = 2

    if screen.cursor.x == 0:
        screen.cursor.bg = tab_bg
        screen.draw(" ")
        start_draw = 1

    if (
        tab.is_active or getattr(extra_data.prev_tab, "is_active", False)
    ) and start_draw != 1:
        screen.cursor.bg = tab_bar_background
        screen.cursor.fg = tab_bg
        screen.draw(back_separator_symbol)

    screen.cursor.bg = tab_bg
    if min_title_length >= max_tab_length:
        screen.draw("…")
    else:
        if tab.has_activity_since_last_focus and getattr(
            extra_data.prev_tab, "is_active", False
        ):
            screen.cursor.fg = tab_bar_background
        screen.draw(" ")
        draw_title(draw_data, screen, tab, index - 1, max_tab_length)
        screen.draw(" ")
        extra = screen.cursor.x + start_draw - before - max_tab_length
        if extra > 0 and extra + 1 < screen.cursor.x:
            screen.cursor.x -= extra + 1
            screen.draw("…")
        screen.cursor.fg = tab_bg
        screen.cursor.bg = next_tab_bg
        if tab.is_active or getattr(extra_data.next_tab, "is_active", False):
            screen.cursor.bg = tab_bar_background
        screen.draw(separator_symbol)
    end = screen.cursor.x
    if end < screen.columns:
        screen.draw(" ")
    return end
