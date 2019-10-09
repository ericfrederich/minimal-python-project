import pathlib


def format_file(title, text):
    return f"### `{title}`\n" "```python\n" + text + "```\n\n"


strings = []
for file in pathlib.Path().rglob("*.py"):
    strings.append(format_file(file.name, file.read_text()))

tree = (
    "\n```\n"
    + "\n".join("python-greeter/" + str(p) for p in pathlib.Path().rglob("*.py"))
    + "\n```\n"
)

output = pathlib.Path("input/header.md").read_text() + tree + "".join(strings)

pathlib.Path("README.md").write_text(output)
