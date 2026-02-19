import click
from .core import start_watching

@click.command()
@click.argument('path', default='src/')
def cli(path: str) -> None:
    """CLI tool to watch a directory and format Python files on save."""
    start_watching(path)

if __name__ == "__main__":
    cli()