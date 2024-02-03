from catppuccin import Flavour
from dataclasses import fields

flavour = Flavour.mocha()

for field in fields(flavour):
    item = getattr(flavour, field.name)
    print(f"fish_color_{field.name} {item.hex}")
