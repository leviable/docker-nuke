import click

from . import nuke


@click.command()
@click.option('--force/--no-force', default=False)
def cli(force):
    nuke(force=force)
