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
    while True:
        yield wave_data

tone_gen = generate_tone(220, 44100)

for i in range(5):
    stream.write(next(tone_gen))

stream.stop_stream()
stream.close()
p.terminate()

