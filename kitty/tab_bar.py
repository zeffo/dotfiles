# pyright: reportMissingImports=false
# pyright: reportGeneralTypeIssues=false

import random

from kitty.fast_data_types import Color, Screen, get_options
from kitty.tab_bar import (DrawData, ExtraData, TabBarData, as_rgb,
                           draw_tab_with_powerline, draw_title)
from kitty.utils import color_as_int

opts = get_options()

flavor = {
    "rosewater": (245, 224, 220),
    "flamingo": (242, 205, 205),
    "pink": (245, 194, 231),
    "mauve": (203, 166, 247),
    "red": (243, 139, 168),
    "maroon": (235, 160, 172),
    "peach": (250, 179, 135),
    "yellow": (249, 226, 175),
    "green": (166, 227, 161),
    "teal": (148, 226, 213),
    "sky": (137, 220, 235),
    "sapphire": (116, 199, 236),
    "blue": (137, 180, 250),
    "lavender": (180, 190, 254),
    "text": (205, 214, 244),
    "subtext 1": (186, 194, 222),
    "subtext 0": (166, 173, 200),
    "overlay 2": (147, 153, 178),
    "overlay 1": (127, 132, 156),
    "overlay 0": (108, 112, 134),
    "surface 2": (88, 91, 112),
    "surface 1": (69, 71, 90),
    "surface 0": (49, 50, 68),
    "base": (30, 30, 46),
    "mantle": (24, 24, 37),
    "crust": (17, 17, 27),
}
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
    color = Color(*flavor[field], alpha=2)
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
