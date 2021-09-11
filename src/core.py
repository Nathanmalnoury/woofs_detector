from pathlib import Path
import subprocess

DIR_WAW_PATH = Path("~/Videos/sound_tracks/")


def to_wav_file(path: Path):
    """Extract audio from file to a wav file."""
    subprocess.call(
        f"ffmpeg -i {str(path)} -y -ab 160k -ac 2 -ar 44100 -vn {str(DIR_WAW_PATH / path.name ) + '.wav'}",
        shell=True,
    )
