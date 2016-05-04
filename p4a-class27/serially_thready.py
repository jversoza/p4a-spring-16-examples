"""
A process is your running program, along with the resources necessary to run your program (such as memory space, some sort of unique identifier, environment variables, open file objects, etc.). A process has at least one _thread_ of execution. Think of a thread as an independant sequence of execution. A process can have multiple threads.

If everything is in a single thread, then your program is executed linearly... and if one step takes a long time, it blocks the execution of the rest of your program.

However, if your program has multiple threads, it can have multiple _lines_ of execution... so that _it looks like more than one thing is happening at once_.

We'll use threading to get input serially while showing our turtle animation.
"""
import serial
import threading 
import time

port = '/dev/cu.usbserial-A6008d9E'
baud = 9600
connected = False

ser = serial.Serial(port, baud, timeout=1)

def read_from_port(sio):
    while True:
        serial_line = ser.readline()
        try: 
            val = int(serial_line.decode('utf-8').strip())
            print(val)
        except Exception as e:
            print(e)
    ser.close()

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.start()

while True:
    print("hello")
    time.sleep(0.2)

