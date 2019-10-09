"""Generate the readme from the files in this repository.

Generating it automatically helps ensure that the readme stays in synch with the files.

"""

import pathlib


def format_file(title, text):
    return f"### `{title}`\n" "```python\n" + text + "```\n\n"


strings = []
tree = []
for file in pathlib.Path().rglob("*.py"):
    if str(file) == __file__:
        continue
    strings.append(format_file(file.name, file.read_text()))
    tree.append("python-greeter/" + str(file))

tree_str = "```\n" + "\n".join(tree) + "\n```\n"
output = pathlib.Path("input/header.md").read_text() + tree_str + "".join(strings)

pathlib.Path("README.md").write_text(output)
