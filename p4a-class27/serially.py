"""
serial communication - sending one bit at a time

* uses module called pyserial
* reads in bytes object
* serial over usb connection
"""
import serial

ser = serial.Serial('/dev/cu.usbserial-A6008d9E', 9600)

while True:
    serial_line = ser.readline()
    try: 
        val = int(serial_line.decode('utf-8').strip())
        print(val)
    except:
        pass
            
ser.close() 
