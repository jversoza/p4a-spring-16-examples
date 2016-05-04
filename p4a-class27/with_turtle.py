import turtle
import serial
import time
import threading

t = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
wn.tracer(0)
WIDTH, HEIGHT = 500, 500
wn.setup(WIDTH, HEIGHT)
x, y, w, h, v = -300, 0, 50, 50, 3

readings = [0] * 100
def draw_rect(t, x, y, w, h, color='#7777aa'):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

def next_frame():
    t.clear()
    global x
    color = '#228855'
    x = sum(readings) // len(readings)
    draw_rect(t, x, y, w, h, color=color)
    #x += v
    #if x > WIDTH / 2:
    #    x = - WIDTH / 2
    wn.ontimer(next_frame, 10)

port = '/dev/cu.usbserial-A6008d9E'
baud = 9600
connected = False

ser = serial.Serial(port, baud, timeout=1)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))



def read_from_port(sio):
    global x
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
            print(val)
            x = val - 300
            readings.append(x)
            del readings[0]
        except Exception as e:
            print(e)
    ser.close()

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.start()

next_frame()
wn.mainloop()
