# cli.py
import click

from greetings import app


commands = [
    click.Command("morning", callback=app.morning),
    click.Command("evening", callback=app.evening),
]
cli = click.Group(commands={c.name: c for c in commands})
