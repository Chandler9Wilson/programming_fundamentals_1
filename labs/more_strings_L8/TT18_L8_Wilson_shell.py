# Name: Chandler Wilson
# Date: 07/18/2018
# COSC1336, Lab 8, shell output
>>> print('hello world
  File "<stdin>", line 1
    print('hello world
                     ^
SyntaxError: EOL while scanning string literal
>>> print('hello world')
hello world
>>> hello = list('hello world')
>>> for letter in hello:
...     print(letter, end='')
...
hello world>>> /n
  File "<stdin>", line 1
    /n
    ^
SyntaxError: invalid syntax
>>> \n
  File "<stdin>", line 1
    \n
     ^
SyntaxError: unexpected character after line continuation character
>>>
>>> hello.index('h')
0
>>> try:
...     hello.index('x')
... except:
...     print('That probably doesn't exist')
  File "<stdin>", line 4
    print('That probably doesn't exist')
                               ^
SyntaxError: invalid syntax
>>> try:
...     hello.index('x')
... except:
...     print("That probably doesn't exist")
...
That probably doesn't exist
>>> len(hello)
11
>>> hello2 = hello + hello
>>> hello += 'hmmm'
>>> if hello == hello2:
...     print('something went wrong')
...
>>> hello3 = 'hello how are you doing?'
>>> ' '.slice(hello3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'slice'
>>> hello3[5:]
' how are you doing?'
>>> hello3[6:]
'how are you doing?'
>>> hello3[6:12:3]
'h '
>>> if 'hello' in hello3:
...     print("I'm polite")
...
I'm polite
>>> hello3.isalnum
<built-in method isalnum of str object at 0x7f5c44631df0>
>>> hello3.isalnum()
False
>>> hello3.isalpha()
False
>>> 'asdf'.isapha()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isapha'
>>> 'asdf'.isalpha()
True
>>> 'asd123'.isalnum()
True
>>> 'asdf'.isdigit()
False
>>> '123'.isdigit()
True
>>> '123'.islower()
False
>>> 'adf'.islower()
True
>>> 'adf'.isspace()
False
>>> ' '.isspace()
True
>>> 'hello world'.isspace()
False
>>> 'abc'.isupper()
False
>>> 'ABC'.isupper()
True
>>> 'ABC'.lower()
'abc'
>>> ' abc'.lstrip()
'abc'
>>> 'abc '.rstrip()
'abc'
>>> ' '.strip('hello world ')
''
>>> 'hello world '.strip(' ')
'hello world'
>>> hello.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
>>> hello3.upper()
'HELLO HOW ARE YOU DOING?'
>>> hello3.endswith()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: endswith() takes at least 1 argument (0 given)
>>> hello3.endswith(' ')
False
>>> hello3.endswith('?')
True
>>> hello3.endswith('doing?')
True
>>> hello3.find(' ')
5
>>> hello3.replace(' ', '?')
'hello?how?are?you?doing?'
>>> hello3.startswith()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: startswith() takes at least 1 argument (0 given)
>>> hello3.startswith(' ')
False
>>> hello3.startswith('h')
True
>>> hello3 * 3
'hello how are you doing?hello how are you doing?hello how are you doing?'
>>> 'mhmmm' * 20
'mhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmmmhmmm'
>>> 'mhmm'.split('h')
['m', 'mm']
>>> hello3.join(' ')
' '
>>> hello3.join()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: join() takes exactly one argument (0 given)
>>> hello3.join('h')
'h'
>>> ' '.join(hello3)
'h e l l o   h o w   a r e   y o u   d o i n g ?'
>>> def hr():
...     print('-' * 30)
...
>>> hr()
------------------------------
>>> def strip_spaces():
...
...
  File "<stdin>", line 3

    ^
IndentationError: expected an indented block
>>>
>>> def strip_spaces(to_strip):
...     if to_strip
  File "<stdin>", line 2
    if to_strip
              ^
SyntaxError: invalid syntax
>>> '$%^'.isalpha()
False
>>> '\0'.isalpha()
False
>>> '\0'.islower()
False
>>> '\0'.isupper()
False
>>> '\0'.ispace()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'ispace'
>>> '\0'.isspace()
False
>>> '\0'.lower()
'\x00'
>>> '\0'.upper()
'\x00'
>>> '\0'.strip()
'\x00'
>>> '\0'.strip(' ')
'\x00'
>>> '\0'.strip('\0')
''
>>> hello3.replace('hello', 'screw you')
'screw you how are you doing?'
>>> if hello3.startswith('screw you'):
...     print('Thats pretty rude')
...
>>> def how_polite(string):
...     if string.startswith('hello'):
...             print('How polite')
...     elif string.startswith('screw you'):
...             print('Thats pretty rude')
...
>>> how_polite('screw you')
Thats pretty rude
>>> how_polite('hello')
How polite
>>>
