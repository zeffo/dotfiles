fmt = "\u001b[38;5;13m  \u001b[38;5;183m  \u001b[38;5;9m  \u001b[38;5;216m  \u001b[38;5;11m  \u001b[38;5;10m  \u001b[38;5;6m  \u001b[38;5;117m  \u001b[38;5;12m  \u001b[38;5;147m "


chunks = fmt.split()

final = "  ".join(chunks) + "    " + "  ".join(chunks[::-1])
final = final.replace("\u001b", "\\u001b")
print(final)
