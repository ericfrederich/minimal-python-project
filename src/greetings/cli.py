# cli.py
import click

from greetings import app

@click.group()
def cli():
    pass


@cli.command()
def morning(**kwargs):
    app.morning(**kwargs)


@cli.command()
def evening(**kwargs):
    app.evening(**kwargs)
