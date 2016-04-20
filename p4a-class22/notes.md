Administrative Stuff
-----
* demo homework 
* likely last required assignment / final project from here on in
* last assignment will be optional (submit to replace low/missing hw score) on iterators, generators and inheritance
* milestone #1

Review on OOP
-----
* review composition 
* review ducktyping / polymorphism
* review inheritance, multiple inheritance

Inheritance cont
-----
* person, teacher, student, grad student
* exceptions

Inheritance vs Composition
-----
* two different techniques to describe two different relationships
    * a Rectangle is a Polygon
    * a Polygon has a (multiple) Point
* sometimes you can use either, though!
* see [online reading](http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-1-objects-and-types/#.Vws3NBMrKRs)
* example: door vs lockabledoor
    * default closed
    * open
    * get_status
    * close

More magic variables ()
-----
* dynamically accessing attributes
    * getattr
    * hasattr
* attribute lookup
    * \_\_dict\_\_
    * then __class__
    * if not, then call \_\_getattr\_\_

Example using Pig game?
-----
* functional version
* object oriented version? 

Iterators
-----
* what can we loop over?
* for loops examples
    * for ch in "word"
    * for i in range(5)
    * for ele in (1, 2, 3)
    * for ele in [1, 2, 3]
    * for k, v in {'x':1, y:2}
* how does this work?
    * for calls iter() which uses __iter__ on the container object
    * returns an iterator object that implements the following method
    * prove it! hasattr __iter__
    * usually iterator object and container object are _sort of_ same thing
    * you can call next func on iterator object
    * which is really just calling __next__ method
* ok, how to make our own? ... nice syntax
    * implement __iter__ which returns an iterator object
    * iterator object must implement __next__
* finite iterators
    * raise StopIteration
    * reverse string
        * init w/ data
        * start with index = i
        * 
    * range _like_
        * different from list
        * count by 2's
* infinite iterators
    * infinite count (it's not range!)
    * maybe iterator that produces primes (keep on adding ... is_prime)
    * vs call next a few times
* using generators to create iterators
    * just a funciton
    * yield returns value and pauses function
* zip, multiple lists
    * iterator over tuples with element from each
    * try multiple!
* count
* generator expressions
    * use zip 
    * print out the sum of two arrays
* why not just use list?

pyaudio

```
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
```
```

A sample rate of 44.1 kHz is 44,100 samples/second
A 1 kHz wave is 1,000 cycles/second
The sine function has a cycle length of 2*pi
So. You need to scale your sine function such that 1,000 sine wave cycles would fit into 44,100 samples. Here's a rough look at how you'd derive code to fill the buffer:
// via https://www.daniweb.com/programming/software-development/threads/354944/creating-a-sine-wave-at-a-specific-frequency-and-sample-rate
  // i is the sample index
  // Straight sine function means one cycle every 2*pi samples:
  // buffer[i] = sin(i); 
  // Multiply by 2*pi--now it's one cycle per sample:
  // buffer[i] = sin((2 * pi) * i); 
  // Multiply by 1,000 samples per second--now it's 1,000 cycles per second:
  // buffer[i] = sin(1000 * (2 * pi) * i);
  // Divide by 44,100 samples per second--now it's 1,000 cycles per 44,100
  // samples, which is just what we needed:
  buffer[i] = sin(1000 * (2 * pi) * i / 44100);
```
 

