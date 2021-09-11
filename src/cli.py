from pathlib import Path
from core import to_wav_file
import click


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
def loud_sounds_finder(path):
    print("hello")
    to_wav_file(path)


if __name__ == "__main__":
    loud_sounds_finder()
