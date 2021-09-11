from pathlib import Path
from pprint import pprint, pformat

import click
from numpy.distutils.misc_util import green_text

from src.file_handler import FileHandler
from src.wav_processor import process


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
def loud_sounds_finder(path):
    file_handler = FileHandler(path)
    click.secho('Extracting audio...', fg='blue')
    file_handler.create_required_dir()
    file_handler.convert_file_to_wav()
    click.secho('Extraction done.\nstarting processing:', fg='blue')
    data = process(file_handler.soundtrack_file_path)
    click.secho('Cleaning up...')
    file_handler.clean_up()

    click.secho(pformat(data))
