import math
import numpy
import pyaudio


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    res = numpy.sin(numpy.arange(length) * factor)
    return res


def play_tone(stream, frequency=440, length=5, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))

    #print(chunks)
    chunk = numpy.concatenate(chunks) 
    print(chunk)
    #print(chunk.astype(numpy.float32).tostring())
    stream.write(chunk.astype(numpy.float32).tostring())


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)

    play_tone(stream)

    stream.close()
    p.terminate()
