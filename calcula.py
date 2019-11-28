from pydub import AudioSegment
from numpy import log10


def calcular_db(filename="file.wav"):
    sound = AudioSegment.from_file(filename, format="wav")
    peak_amplitude = sound.max
    return (20 * log10(peak_amplitude)) - 20 # margem de correção

