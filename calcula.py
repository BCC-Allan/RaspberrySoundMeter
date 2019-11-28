from pydub import AudioSegment
from numpy import log10


sound = AudioSegment.from_file("file.wav", format="wav")
peak_amplitude = sound.max

print(peak_amplitude)
print(sound.max_possible_amplitude)

print(20 * log10(peak_amplitude))