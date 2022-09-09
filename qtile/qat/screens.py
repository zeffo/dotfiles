from libqtile import bar, widget
from libqtile.config import Screen

from qat.settings import palette

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=18,
    background=palette["base"],
    foreground=palette["surface0"],
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='text',
                    this_current_screen_border = palette['yellow'],
                    active = palette['blue'],
                    background = palette["base"],
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground=palette["text"],
                    background=palette['mantle'],
                    padding=0,
                    fontsize = 35,
                    ),
                widget.WindowName(
                    background = palette['mantle'],
                    format = "{name}",
                    foreground = palette['surface1'],
                    empty_group_string = 'Desktop',
                    width = 320,
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    background=palette["rosewater"],
                    foreground=palette['mantle'],
                    padding=0,
                    fontsize = 35,
                    ),
                widget.Net(
                    background = palette["lavender"],
                    foreground = palette['surface1'],
                    format = "{down} ↓↑ {up}",
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    background=palette['crust'],
                    foreground=palette["mauve"],
                    padding=0,
                    fontsize=35,
                    ),
                widget.Prompt(
                    prompt = "Run:",
                    foreground=palette['teal']
                    ),
                widget.Spacer(),
                widget.TextBox(
                    text='',
                    foreground=palette['mantle'],
                    padding=-15,
                    fontsize=108
                    ),
                 widget.TextBox(
                    text='',
                    background=palette['mantle'],
                    foreground=palette['blue'],
                    padding=-15,
                    fontsize=108
                ),
                widget.CurrentLayoutIcon(
                        background=palette['blue'],
                        padding = 0,
                        scale = 0.5,
                        ),
                widget.CurrentLayout(
                    background=palette['blue'],
                ),
                widget.TextBox(
                    text='',
                    background=palette['blue'],
                    foreground=palette['pink'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.CPU(
                    background=palette['pink'],
                    format = '  {load_percent}%'
                    ),
                widget.TextBox(
                    text='',
                    background=palette['pink'],
                    foreground=palette['peach'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.Memory(
                    background=palette['peach'],
                    format='  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    measure_mem='G'
                        ),
                widget.TextBox(
                    text='',
                    background=palette['peach'],
                    foreground=palette['green'],
                    padding=-15,
                    fontsize=108
                ),
                widget.TextBox(
                    text='墳 ',
                    background=palette['green'],
                    padding=0,
                    ),
                widget.PulseVolume(
                    background=palette['green'],
                    ),
                widget.TextBox(
                    text='',
                    background=palette['green'],
                    foreground=palette['yellow'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.Clock(
                        format='  %I:%M %p',
                        background=palette['yellow'],
                        ),
                widget.Systray(
                    icon_size = 30
                        ),
            ],
            39,
            margin = [9, 9, 9, 9],
        ),
    ),
]