import struct
import pyaudio
import math
p = pyaudio.PyAudio()
rate = 44100
channels = 1

stream = p.open(
        format=pyaudio.paFloat32,
        channels=channels,
        rate=rate,
        output=True)


def generate_tone(freq, rate):
    data = []
    for i in range(rate):
        #data.append(math.sin(i / 200 * 2 * math.pi))
        data.append(math.sin(freq * (2 * math.pi) * i / rate));
    wave_data = b''.join([struct.pack('f', d) for d in data])
    return wave_data

stream.write(generate_tone(220, 44100))
stream.write(generate_tone(246.94, 44100))
stream.write(generate_tone(261.63, 44100))
stream.write(generate_tone(293.66, 44100))
stream.write(generate_tone(329.63, 44100))
stream.write(generate_tone(349.23, 44100))
stream.write(generate_tone(392.00, 44100))
stream.stop_stream()
stream.close()
p.terminate()
