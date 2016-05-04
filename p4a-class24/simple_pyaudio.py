"""
some definitions again (from think dsp, http://greenteapress.com/thinkdsp/html/thinkdsp002.html):

signals
-----
* a signal represents a quantity that varies in time, or space, or both
* working with sound generated by computers is sometimes called _digital_ signal processing
* why? sound is variation in air pressure - a sound signal represents variations in air pressure over time
* (remember it's a pressure wave that causes our ear drums to vibrate)
* speakers generate these pressure waves by taking an eletrical signal (yes, another signal) and converting it to a signal in another form
* apparently, signals can also represent a quantity that varies in space (elevation along a hiking trail)... and also have more than 1 dimension (like a 2d image or a movie that varies in 2d space and time)

periodic signals
-----
* signals that repeat themselves over some period in time
* an example is a sin wave (clearly repeats!)
* a single repetition is called a __cycle__
* the duration of a cycle is called the __period__
* __frequency__ is the number of cycles per second ( inverse of a period) ... measured in Hz
* for example, if we have 1 second... and our signal contains 9 full cycles / periods... then the frequency is 9 Hz
    * (that's probably to low of a tone to hear!)
    * see later notes
* in previous class we saw we could sum waves
* it turns out we can express _any_ signal by summing sin waves with different frequencies (!?)

pitch and volume
-----
* periodic signals are interesting because we hear them as _clear tones_ with a definite pitch
* __freqency__ number of repetitions/cycles per second affects pitch... for example 440 Hz, is a higher pitched tone than 220 Hz
* remember our example of 9 hz before?
    * (from previous class, we discussed that humans can _hear_ up to 20000 Hz)
    * range is usually from 20 Hz and 15000 Hz)
    * (children can hear up to 20000 Hz)
    * (me, probably only like 10000 Hz)
    * should we test this?
* __gain__ or volume is controlled by amplitude


sampling
-----
* computers only deal with numbers
* digital to analog conversion - converts numbers into electrical signals (hey, we have signals again), causes a speaker membrane to vibrate
* numbers to membrane positions:
    * outer most, most convex is a 1
    * at rest is 0
    * inner most, most concave is a -1 
    * some values inbetween
* these fluctuations of a membrane can be graphed:
    * time on the x axis
    * position on the y axis
    * sin
    * square 
    * sawtooth (ramp up, and drop immediately)
    * triangle (ramp up, ramp down)
* a single, individual number (speaker position) at a particular time is called a __sample__
* the number of samples we take per second is called the __sample rate__
* (note that this is different from frequency, which is number of cycles/periods/repetitions per second)
* imagine chopping up our wave into very small slices
* it turns out... that the max frequency that can be represented at any given sampling rate is half the sampling rate
* what does that mean?
* for a 20000 Hz, we'd need 40000 samples per second (also measure in Hz)
    * so 44100 Hz was initially used as the sampling rate for CDs
    * and is pretty common now
    * why do we use?
* above 1 or below -1... will be clipped (will approach square wave for periodic signal like sin!)
* what about clicks? ... usually produced from a jolt
    * ramp up or down
* so... if a signal has a frequency of, let's say 440 Hz, that is 440 cycles per second

pyaudio is a python module that is an interface to 
portaudio .... interface to your underlying sound device <-- C/++

streams - write numbers directly to a sound device (or read)
a stream can be input, output... or even both

we want to write bytes to a stream to produce audio

i have struct as an import... because we need bytes
math... because sin (and also pi)

this is inefficient (because there are a lot of extra operations being done)
better: use numpy
"""
import struct
import pyaudio
import math
"""
set up audio system (uses underlying library called portaudio)
"""
p = pyaudio.PyAudio()


"""
open a stream
 takes some configuration parameters (as keyword args)
 * rate - (sample rate) (44.1 khz)
 * blocking - True (won't let program go on until audio is finished processing)
 * format - what number format are we using when we write bytes (32 bit floats)
 * channel - number of output devices / "tracks", mono (1 channel) vs stereo (2 channel)
"""

"""
opens a stream to your audio device - which can be input, output or both
there are a bunch of options
we're using:
* rate - sampling rate, we'll use 44.1 khz (1 second of audio chopped up into 44100 pieces)
* format - the format that the data will be in ... 32 bit float
* channels - number of "tracks", "channels", actual devices; think mono (1) vs stereo (2)
* output - is this an output stream?
* blocking
"""
rate = 44100
channels = 1

"""
stream represents an input / output or both
and once we have that... we can go ahead and start writing data
"""
stream = p.open(
        format=pyaudio.paFloat32,
        channels=channels,
        rate=rate,
        output=True)

"""
generate a lot of numbers
questions... how long will this play?

what will these play?

1. just write a lot of ones
2. write either 1's or -1's
(1 for 100 samples, -1 for 100 samples, etc.)
what's the frequency?
 1    _   _   _   _
 0   | | | | | | |
-1  _| |_| |_| |_|

square wave - "hollow", ramps up and down instantly and hold value
"""
#values = [-1, 1]
values = [0, 1]
data = []
for i in range(44100):
    # 1 a bunch of ones...
    # data.append(1)

    # 2 only -1 or 1
    #data.append(values[i // 100 % 2])
    pass

"""
3. ramp up and drop
saw tooth ("harsh" sound)

 1
 0  /| /| /| /| /|
-1 / |/ |/ |/ |/ |
"""
# 3 ramp up, then drop
for i in range(221):
    for j in range(-100, 101):
        #data.append(j / 100)
        pass


"""
# i is sample index (think of it as time)
# so... if we have a sin function, it repeats for 2*pi samples
# here's one sample
# data[i] = sin(i); 

# Multiply by 2*pi--now it's one cycle per sample:
# data[i] = sin((2 * pi) * i); 

# Multiply by 221 cycles 
# data[i] = sin(221 * (2 * pi) * i);

# Divide by 44,100 samples per second--now it's 221 cycles per 44,100 samples
#
# data[i] = sin(221 * (2 * pi) * i / 44100);
221 /44100
~ 0.05

/200
~ 0.05

why / 200?
we have 44100 samples
i want cycle to repeat ~221 in those 44100
so every 200 samples should represent 1 cycle
"""
for i in range(44100):
    #data.append(math.sin(i / 200 * 2 * math.pi))
    data.append(math.sin(221 * (2 * math.pi) * i / 44100));
    pass


"""
* write takes a byte stream
* (so we end up using bytes string data type)
* struct.pack turns floats into bytes
    * see... really!
    * type(struct.pack('f', 0.123))
* we can use join
"""
wave_data = b''.join([struct.pack('f', d) for d in data])
stream.write(wave_data)

stream.stop_stream()
stream.close()
p.terminate()


"""
this processing takes a lot of time!
first... generating 44100 samples
turning each one into bytes!
lots of memory and computation
"""
