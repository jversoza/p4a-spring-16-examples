import math
import struct
import pyaudio

p = pyaudio.PyAudio();
stream = p.open(
        rate=44100,
        channels=1,
        output=True,
        format=pyaudio.paFloat32
        )
"""make a bunch of numbers!!!!"""

"""
stream.write <-- takes bytes
when we pass in a bunch of floats (as a single bytes object) ... we have to do a conversion
"""
import random
""" index into this with either 0 or 1"""
values = [-1, 1]
data = []
#~220 Hz
for i in range(44100):
    data.append(values[i // 100 % 2])

for i in range(221):
    for j in range(-100, 101):
        data.append(j / 100)

for i in range(44100):
    data.append(math.sin(i / 200 * 2 * math.pi))
    #data.append(math.sin(221 * (2 * math.pi) * i / 44100));

print(len(data))
#print(data[0:400])

# how many elements should be in data?


"""
make bytes objects out of this list of numbers (floats)
"""
wave_data = b''.join([struct.pack('f', number) for number in data])

stream.write(wave_data)

stream.stop_stream()
stream.close()
p.terminate()








