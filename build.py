import pathlib


def format_file(title, text):
    return f"### `{title}`\n" "```python\n" + text + "```\n\n"


strings = []
for file in pathlib.Path().rglob("*.py"):
    strings.append(format_file(file.name, file.read_text()))

output = pathlib.Path("input/header.md").read_text() + "".join(strings)

pathlib.Path("README.md").write_text(output)
