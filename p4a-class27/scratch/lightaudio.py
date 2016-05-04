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
    for i in range(rate * 5):
        #data.append(math.sin(i / 200 * 2 * math.pi))
        data.append(math.sin(freq * (2 * math.pi) * i / rate));
    return data

def add(freqs, rate):
    freqs_data = [generate_tone(freq, rate) for freq in freqs]
    combined = [sum(t) * 0.25 for t in zip(*freqs_data)]
    wave_data = b''.join([struct.pack('f', d) for d in combined])
    """
    while True:
        yield wave_data
    """
    return wave_data

#tone_gen = add([200, 202], 44100)


import serial
import threading
import struct
import time
import io

port = '/dev/cu.usbserial-A6008d9E'
baud = 9600
connected = False

ser = serial.Serial(port, baud, timeout=1)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


def handle_data(serial_in):
    global data
    data = serial_in
    print(data)
    
freq = 200

def read_from_port(sio):
    global freq
    while True:
        #stream.write(next(tone_gen))
        serial_line = ser.readline()
        try: 
            val = int(serial_line.decode('utf-8').strip())
            """
            if '\r\n' not in val:
                ser.readline()
                serial_line = ser.readline()
                val = int(serial_line.decode('utf-8').strip())
            print(val)
            """
            freq = val // 2
            print(freq)
            time.sleep(1)
        except Exception as e:
            print(e)
    ser.close()

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.start()

while True:
    wave_data = add([freq, freq + 2], 44100)
    stream.write(wave_data)

stream.stop_stream()
stream.close()
p.terminate()

"""
import serial

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

sample_num = 0

def generate_tone(freq, rate):
    #global sample_num
    data = []
    #for i in range(rate // 1000):
    for i in range(rate):
        #if sample_num >= rate:
        #    sample_num = 0

        #data.append(math.sin(i / 200 * 2 * math.pi))
        #data.append(math.sin(freq * (2 * math.pi) * sample_num / rate));
        data.append(math.sin(freq * (2 * math.pi) * i / rate));
        #sample_num += 1
    return data

def add(freqs, rate):
    freqs_data = [generate_tone(freq, rate) for freq in freqs]
    combined = [sum(t) * 0.25 for t in zip(*freqs_data)]
    wave_data = b''.join([struct.pack('f', d) for d in combined])
    return wave_data


#ser = serial.Serial('/dev/cu.usbserial-A6008d9E', 9600)

while True:
    #stream.write(next(tone_gen))
    #serial_line = ser.readline()
    try: 
        #val = int(serial_line.decode('utf-8').strip()) 
        #freq = val // 2
        freq = 200
        #print(freq)
        data = add([200, 202], 44100)
        stream.write(data)
    except:
        pass
            
ser.close() # Only executes once the loop exits

stream.stop_stream()
stream.close()
p.terminate()
"""
