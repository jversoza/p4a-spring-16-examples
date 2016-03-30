
# Bytes

A bytes object is a sequence of single bytes. Bytes objects are immutable. To create a literal byte, prefix a string (before the quote) with a lowercase b: `b'hello'`

Although bytes look like strings, they're actually _just_ bytes, not actually strings. To use them as a string, we have to __decode__ them.

[Check out the official Python documentation on bytes](https://docs.python.org/3/library/stdtypes.html#bytes) read through the examples below: 

```python
>>> bytes
<class 'bytes'>
>>> b'hello'
b'hello'
>>> b = b'hello'
>>> b + "world"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't concat bytes to str
>>> b
b'hello'
>>> b.decode('utf-8') 
'hello'
>>> bytes('5', 'utf-8')
b'5'
```

# Print with Keyword Arguments

Print can take an arbitrary number of arguments... and it also accepts keyword arguments:

* `sep` - character that separates arguments when arguments are printed out (default is space)
* `end` - character that gets printed last (default is new line)

```python
>>> print('hello', 'world')
hello world
>>> print('hello', 'world', sep='x')
helloxworld
>>> print('hello', 'world', sep='x', end='.')
helloxworld.>>> s = "hello"
```

# Determining Class / Instance

The following examples show 3 ways of determining the type / class of an object / instance:

1. `type(obj)` - returns type of obj
2. `obj.__type__` - type of obj
3. `isinstance(obj, class_name)` - True if obj is of type class_name, False otherwise


```python
>>> s = 'hello'
>>> type(s)
<class 'str'>
>>> s.__class__
<class 'str'>
>>> isinstance(s, str)
True
>>> isinstance(5, str)
False
```
