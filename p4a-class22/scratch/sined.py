import math
import pyaudio
import struct

"""
def get_wave_data(frequency, amplitude, length, rate):
    number_of_samples = int(length * rate)
    factor = frequency * (math.pi * 2) / rate 
    data = [math.sin(n * factor) for n in range(number_of_samples)]
    wave_data = b''.join([struct.pack('f', d) for d in data])
    return wave_data

def play_tone(frequency, amplitude, length, rate):
    wave_data = get_wave_data(frequency, amplitude, length, rate)
    p = pyaudio.PyAudio()
    stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=rate,
            output=True)

    stream.write(wave_data)
    stream.stop_stream()
    stream.close()
    p.terminate()
 
play_tone(440, 1, 1, 44100)
"""
"""
def get_wave_data(frequency, amplitude, rate):
    factor = frequency * (math.pi * 2) / rate 
    data = [math.sin(n * factor) for n in range(rate)]
    while True:
        wave_data = b''.join([struct.pack('f', d) for d in data])
        yield wave_data

def play_tone(frequency, amplitude, rate, duration):
    wave_data = get_wave_data(frequency, amplitude, rate)
    p = pyaudio.PyAudio()
    stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=rate,
            output=True)

    for data in wave_data:
        stream.write(data)
    #for i in range(5):
    #    stream.write(next(wave_data))

    stream.stop_stream()
    stream.close()
    p.terminate()
 
play_tone(440, 1, 44100, 5)
"""

"""

def get_wave_data(frequency, amplitude, rate):
    factor = frequency * (math.pi * 2) / rate 
    data = [math.sin(n * factor) for n in range(rate)]
    while True:
        yield data

def add(f1, f2, amplitude, rate):
    osc1 = get_wave_data(f1, amplitude, rate)
    osc2 = get_wave_data(f2, amplitude, rate)
    while True:
        d1 = next(osc1)
        d2 = next(osc2)
        data = [x + y for x, y in zip(d1, d2)]
        wave_data = b''.join([struct.pack('f', d) for d in data])
        yield wave_data

def add_all(frequencies, amplitude, rate):
    oscs = [get_wave_data(f, amplitude, rate) for f in frequencies]
    while True:
        nums = [next(osc) for osc in oscs]
        data = [sum(t) * amplitude for t in zip(*nums)]
        wave_data = b''.join([struct.pack('f', d) for d in data])
        yield wave_data

def play_tone(frequency, amplitude, rate, duration):
    #wave_data = add(440, 443, amplitude, rate)
    #wave_data = add_all([440, 443], amplitude, rate)
    wave_data = add_all([440, 443, 445], amplitude, rate)
    #wave_data = add_all([440, 443, 445], amplitude, rate)
    # wave_data = add_all([400, 403, 300, 350], amplitude, rate)
    #wave_data = add_all([400, 403, 300, 302, 305], amplitude, rate)
    #wave_data = add_all([150, 151, 200, 201, 208, 220], amplitude, rate)
    p = pyaudio.PyAudio()
    stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=rate,
            output=True)

    for data in wave_data:
        stream.write(data)
    #for i in range(5):
    #    stream.write(next(wave_data))

    stream.stop_stream()
    stream.close()
    p.terminate()
 
play_tone(440, 1/6, 44100, 5)
"""

import random
def play_noise(rate):
    def noise():
        while True:
            data = [random.uniform(-1, 1) for i in range(1024)]
            wave_data = b''.join([struct.pack('f', d) for d in data])
            yield wave_data
    p = pyaudio.PyAudio()
    stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=rate,
            output=True)
    for data in noise():
        stream.write(data)
    #for i in range(5):
    #    stream.write(next(wave_data))

    stream.stop_stream()
    stream.close()
    p.terminate()
play_noise(44100)
