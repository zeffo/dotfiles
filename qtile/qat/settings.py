from qat.palette import Palette, PaletteType

palette: PaletteType = (
    Palette.mocha
)  # Catppuccin theme (latte, frappe, macchiato, mocha)

terminal: str = "alacritty"  # Default terminal
mod: str = "mod4"  # Mod (super) key
wmname: str = "Qatppuccin"  # WM Name

__all__ = ("terminal", "mod", "wmname", "palette")
