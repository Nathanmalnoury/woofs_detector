from pathlib import Path
import subprocess


class FileHandler:
    def __init__(self, filepath: Path):
        self.path = filepath
        self.soundtrack_directory = self.path.parent / ".soundtrack"
        self.soundtrack_file_path = self.soundtrack_directory / (
            self.path.name + ".wav"
        )

    def create_required_dir(self):
        self.soundtrack_directory.mkdir(parents=True, exist_ok=True)

    def convert_file_to_wav(self):
        """Extract audio from file to a wav file."""
        subprocess.call(
            f"ffmpeg -i {str(self.path)} -y -ab 160k -ac 2 -ar 44100 -vn {str(self.soundtrack_file_path)}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def clean_up(self):
        self.soundtrack_file_path.unlink()
