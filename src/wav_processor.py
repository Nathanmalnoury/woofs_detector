# def decibels()
from pathlib import Path
from typing import List, Dict

import numpy as np
from scipy.io.wavfile import read


def decibel(chunk: np.ndarray) -> float:
    return 20 * np.log10(np.sqrt(np.mean(chunk ** 2)))


def get_loudest_chunks(chunks_decibels: list[float], top: int, chunk_duration: int):
    loudest = sorted(chunks_decibels, reverse=True)[:top]
    data = []
    for intensity in loudest:
        chunk_number = chunks_decibels.index(intensity)
        start_time = chunk_number * chunk_duration
        end_time = (chunk_number + 1) * chunk_duration
        data.append({"db": round(intensity, 2), "start": start_time, "end": end_time})
    return data


def process(wav_path: Path, chunk_duration: int = 5, top: int = 5) -> List[Dict]:
    """
    Cut sound in chunks of given {chunk_duration}, return loudest {top} chunks.
    :return: [{ 'db': intensity in db of chunk, 'start': start time of chunk, 'end': end time of chunk}, ... ]
    """
    samp_rate, wav_data = read(str(wav_path))

    chunks_decibels = get_chunks_decibels(chunk_duration, samp_rate, wav_data)
    top_loudest_chunks = get_loudest_chunks(chunks_decibels, top, chunk_duration)
    return top_loudest_chunks


def get_chunks_decibels(
    chunk_duration: int, samp_rate: float, wav_data: np.ndarray
) -> list[float]:
    """
    Cut data into chunks of given duration, and return a dict { time_start_chunk: decibel(chunk) }
    :param chunk_duration: time in seconds
    :param samp_rate: sample rate in Hertz
    :param wav_data: array [channel_right, channel_left] at each point.
    """
    chunk_size = chunk_duration * samp_rate
    num_chuks = (len(wav_data) // chunk_size) + 1
    chunks = np.array_split(wav_data, num_chuks)
    return [decibel(chunk) for chunk in chunks]
