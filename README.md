# leetcode_python
My Leetcode source code. Python version.


## Hidden Features ([Got from here](http://stackoverflow.com/questions/101268/hidden-features-of-python))

### Numbers:
##### round

		>>> str(round(1234.5678, -2))
		'1200.0'
		>>> str(round(1234.5678, 2))
		'1234.57'


##### Integer base

		>>> int('10', 0)
		10
		>>> int('0x10', 0)
		16
		>>> int('010', 0)  # does not work on Python 3.x
		8
		>>> int('0o10', 0)  # Python >=2.6 and Python 3.x
		8
		>>> int('0b10', 0)  # Python >=2.6 and Python 3.x
		2

##### In-place value swapping

		>>> a = 10
		>>> b = 5
		>>> a, b
		(10, 5)

		>>> a, b = b, a
		>>> a, b
		(5, 10)

------

### String:

##### Multi-line Strings

		>>> sql = "select * from some_table \
		where id > 10"
		>>> print sql
		select * from some_table where id > 10

--

		>>> sql = """select * from some_table
		where id > 10"""
		>>> print sql
		select * from some_table where id > 10

--

		>>> sql = ("select * from some_table " # <-- no comma, whitespace at end
							 "where id > 10 "
							 "order by name")
		>>> print sql
		select * from some_table where id > 10 order by name

##### In

		>>> 'str' in 'string'
		True
		>>> 'no' in 'yes'
		False
		>>>

#####

		''.join(list_of_strings)

##### set

		>>> a = set([1,2,3,4])
		>>> b = set([3,4,5,6])
		>>> a | b # Union
		{1, 2, 3, 4, 5, 6}
		>>> a & b # Intersection
		{3, 4}
		>>> a < b # Subset
		False
		>>> a - b # Difference
		{1, 2}
		>>> a ^ b # Symmetric Difference
		{1, 2, 5, 6}

##### Slice operators

    a = [1,2,3,4,5]
    >>> a[::2]  # iterate over the whole list in 2-increments
    [1,3,5]

--

    >>> a[::-1]
    [5,4,3,2,1]

--

    >>> a = range(10)
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> a[:5] = [42]
    >>> a
    [42, 5, 6, 7, 8, 9]
    >>> a[:1] = range(5)
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> del a[::2]
    >>> a
    [1, 3, 5, 7, 9]
    >>> a[::2] = a[::-2]
    >>> a
    [9, 3, 5, 7, 1]

##### dict's constructor

		>>> dict(foo=1, bar=2)
		{'foo': 1, 'bar': 2}


------

### Args:

##### Use _ instead of last printed item

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> _
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>>

##### *args & **kwargs

    >>> g = lambda *args, **kwargs: args[0], kwargs['thing']
    >>> g(1, 2, 3, thing='stuff')
    (1, 'stuff')

##### Function argument unpacking

		def draw_point(x, y):
				# do some magic

		point_foo = (3, 4)
		point_bar = {'y': 3, 'x': 2}

		draw_point(*point_foo)
		draw_point(**point_bar)

------

### Mulit-operation combain

##### Ternary operator

    >>> 'ham' if True else 'spam'
    'ham'
    >>> 'ham' if False else 'spam'
    'spam'

--

    >>> True and 'ham' or 'spam'
    'ham'
    >>> False and 'ham' or 'spam'
    'spam'

--

    >>> [] if True else 'spam'
    []
    >>> True and [] or 'spam'
    'spam'

##### Conditional Assignment

		x = 3 if (y == 1) else 2

--

		x = 3 if (y == 1) else 2 if (y == -1) else 1

--

		(func1 if y == 1 else func2)(arg1, arg2)

--

		x = (class1 if y == 1 else class2)(arg1, arg2)

--

		[(x, y) for x in range(4) if x % 2 == 1 for y in range(4)]
		[(1, 0), (1, 1), (1, 2), (1, 3), (3, 0), (3, 1), (3, 2), (3, 3)]



------

### List

##### zip

    a = [(1,2), (3,4), (5,6)]
    zip(*a)
    # [(1, 3, 5), (2, 4, 6)]

--

		>>> dict([ ('foo','bar'),('a',1),('b',2) ])
		{'a': 1, 'b': 2, 'foo': 'bar'}

		>>> names = ['Bob', 'Marie', 'Alice']
		>>> ages = [23, 27, 36]
		>>> dict(zip(names, ages))
		{'Alice': 36, 'Bob': 23, 'Marie': 27}


##### Nested list

		[(i,j) for i in range(3) for j in range(i) ]

--

		((i,j) for i in range(4) for j in range(i) )


##### enumerate

		>>> a = ['a', 'b', 'c', 'd', 'e']
		>>> for index, item in enumerate(a): print index, item
		...
		0 a
		1 b
		2 c
		3 d
		4 e

--

		>>> l = ["spam", "ham", "eggs"]
		>>> list(enumerate(l))
		>>> [(0, "spam"), (1, "ham"), (2, "eggs")]
		>>> list(enumerate(l, 1))
		>>> [(1, "spam"), (2, "ham"), (3, "eggs")]

##### generators objects

		x = [n for n in foo if bar(n)]

--

		>>> n = ((a,b) for a in range(0,2) for b in range(4,6))
		>>> for i in n:
		...   print i

		(0, 4)
		(0, 5)
		(1, 4)
		(1, 5)

##### iteration ([itertools](http://docs.python.org/library/itertools.html)) & constructor (yield)

		>>> def g(n):
		...     for i in range(n):
		...             yield i **2
		>>> t = g(5)
		>>> t.next()
		0
		>>> t.next()
		1
		>>> t.next()
		4
		>>> t.next()
		9
		>>> t.next()
		16
		>>> t.next()
		Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
		StopIteration

--

		def fab(max):
				a,b = 0,1
				while a < max:
						yield a
						a, b = b, a+b

		>>> for i in fab(20):
		...     print i,",",
		...
		0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 ,

--

		>>> i = (1,2,3,4,5,6,7,8,9,10) # or any iterable object
		>>> iterators = [iter(i)] * 2
		>>> iterators[0].next()
		1
		>>> iterators[1].next()
		2
		>>> iterators[0].next()
		3

--

		def grouper(n, iterable, fillvalue=None):
				"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
				args = [iter(iterable)] * n
				return izip_longest(fillvalue=fillvalue, *args)

--

		>>> from itertools import *
		>>> l = [[1, 2], [3, 4]]
		>>> list(chain(*l))
		[1, 2, 3, 4]

##### Generate List

		>>> from functools import partial
		>>> bound_func = partial(range, 0, 10)
		>>> bound_func()
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		>>> bound_func(2)
		[0, 2, 4, 6, 8]



------

### Statement

##### for...else...

		for i in foo:
				if i == 0:
						break
		else:
				print("i was never 0")

--

		found = False
		for i in foo:
				if i == 0:
						found = True
						break
		if not found:
				print("i was never 0")


##### Context managers and the "with" Statement

		from __future__ import with_statement

		with open('foo.txt', 'w') as f:
				f.write('hello!')

##### Exception else

		try:
			put_4000000000_volts_through_it(parrot)
		except Voom:
			print "'E's pining!"
		else:
			print "This parrot is no more!"
		finally:
			end_sketch()

------

### Funcs:

##### dir

		>>> dir("foo")
		['__add__', '__class__', '__contains__', (snipped a bunch), 'title',
		 'translate', 'upper', 'zfill']

--

		>>> help("foo".upper)
				Help on built-in function upper:

		upper(...)
				S.upper() -> string

				Return a copy of the string S converted to uppercase.

##### Convenient Web-browser controller

		>>> import webbrowser
		>>> webbrowser.open_new_tab('http://www.stackoverflow.com')

##### Built-in http server

		python -m SimpleHTTPServer 8000

##### An interpreter within the interpreter

		$ python
		Python 2.5.1 (r251:54863, Jan 17 2008, 19:35:17)
		[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
		Type "help", "copyright", "credits" or "license" for more information.
		>>> shared_var = "Set in main console"
		>>> import code
		>>> ic = code.InteractiveConsole({ 'shared_var': shared_var })
		>>> try:
		...     ic.interact("My custom console banner!")
		... except SystemExit, e:
		...     print "Got SystemExit!"
		...
		My custom console banner!
		>>> shared_var
		'Set in main console'
		>>> shared_var = "Set in sub-console"
		>>> import sys
		>>> sys.exit()
		Got SystemExit!
		>>> shared_var
		'Set in main console'

##### pretty print

		>>> import pprint
		>>> stuff = sys.path[:]
		>>> stuff.insert(0, stuff)
		>>> pprint.pprint(stuff)
		[<Recursion on list with id=869440>,
		 '',
		 '/usr/local/lib/python1.5',
		 '/usr/local/lib/python1.5/test',
		 '/usr/local/lib/python1.5/sunos5',
		 '/usr/local/lib/python1.5/sharedmodules',
		 '/usr/local/lib/python1.5/tkinter']

------

### Class & Module

##### Creating new types

		>>> NewType = type("NewType", (object,), {"x": "hello"})
		>>> n = NewType()
		>>> n.x
		"hello"

--

		>>> class NewType(object):
		>>>     x = "hello"
		>>> n = NewType()
		>>> n.x
		"hello"

##### Manipulating sys.modules

		>>> import sys
		>>> import ham
		Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
		ImportError: No module named ham

		# Make the 'ham' module available -- as a non-module object even!
		>>> sys.modules['ham'] = 'ham, eggs, saussages and spam.'
		>>> import ham
		>>> ham
		'ham, eggs, saussages and spam.'

		# Now remove it again.
		>>> sys.modules['ham'] = None
		>>> import ham
		Traceback (most recent call last):

--

		>>> import os
		# Stop future imports of 'os'.
		>>> sys.modules['os'] = None
		>>> import os
		Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
		ImportError: No module named os
		# Our old imported module is still available.
		>>> os
		<module 'os' from '/usr/lib/python2.5/os.pyc'>

##### Be careful with mutable default arguments

		>>> def foo(x=[]):
		...     x.append(1)
		...     print x
		...
		>>> foo()
		[1]
		>>> foo()
		[1, 1]
		>>> foo()
		[1, 1, 1]

--

		>>> def foo(x=None):
		...     if x is None:
		...         x = []
		...     x.append(1)
		...     print x
		>>> foo()
		[1]
		>>> foo()
		[1]

## Pythonic
### Got from [here](https://www.quora.com/What-are-some-examples-of-beautiful-Pythonic-code)

--

		def unzip(tuples):
				if tuples:
						return [tuple(t[i] for t in tuples) for i, _ in enumerate(tuples[0])]
				else:
						return []

--

		long_string = "This is a very long string"
		if "long" in long_string:
				print("Match found")

--

		>>> from collections import Counter
		>>> fruits = ['orange', 'banana', 'apple', 'orange', 'banana']
		>>> Counter(fruits)
		Counter({'orange': 2, 'banana': 2, 'apple': 1})


--

		x = ['a', 'b', 'c']

		for index, item in enumerate(x):
				print(index, item)

--

		# A.py

		def filter_items(items):
				for i in items:
						if i < 10:
								yield i


		# B.py

		from A import filter_items as A_filter_items

		def filter_items(items):
				for i in items:
						if i <= 5:
								yield i

		def do_something(items):
				x = A_filter_items(items)
				y = filter_items(items)
				return (x, y)

--

		def add(one, two):
			return one + two

		my_list = [1, 2]
		x = add(*my_list)  # x = 3

		my_dict = {"one": 1, "two": 2}
		y = add(**my_dict) #y = 3

--

		>>> from itertools import zip_longest
		>>> x = [1, 2, 3, 4]
		>>> y = ['a', 'b', 'c']
		>>> for i, j in zip_longest(x, y):
		...     print(i, j)
		...
		1 a
		2 b
		3 c
		4 None

--

		>>> my_dict = {key: value for key, value in zip_longest(x,y)}
		>>> my_dict
		{1: 'a', 2: 'b', 3: 'c', 4: None}

--

		word = #some word
		is_palindrome = word.find(word[-1::-1])

## [PEP8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

----
### Indentation

##### Yes:

    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

    # More indentation included to distinguish this from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    # Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)

##### No:

    # Arguments on first line forbidden when not using vertical alignment.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # Further indentation required as indentation is not distinguishable.
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)

##### Optional:

    # Hanging indents *may* be indented to other than 4 spaces.
    foo = long_function_name(
      var_one, var_two,
      var_three, var_four)

##### If-statemant

    # No extra indentation.
		if (this_is_one_thing and
				that_is_another_thing):
				do_something()

    # Add a comment, which will provide some distinction in editors
    # supporting syntax highlighting.
		if (this_is_one_thing and
				that_is_another_thing):
				# Since both conditions are true, we can frobnicate.
				do_something()

    # Add some extra indentation on the conditional continuation line.
		if (this_is_one_thing
						and that_is_another_thing):
				do_something()o

##### List

	my_list = [
			1, 2, 3,
			4, 5, 6,
			]
	result = some_function_that_takes_arguments(
			'a', 'b', 'c',
			'd', 'e', 'f',
			)

--

	my_list = [
			1, 2, 3,
			4, 5, 6,
	]
	result = some_function_that_takes_arguments(
			'a', 'b', 'c',
			'd', 'e', 'f',
	)


----
### Maximum Line Length

##### Yes:
		with open('/path/to/some/file/you/want/to/read') as file_1, \
				 open('/path/to/some/file/being/written', 'w') as file_2:
				file_2.write(file_1.read())

----
### Should a Line break before or after a binary operator?
##### No: operators sit far away from their operands

	income = (gross_wages +
						taxable_interest +
						(dividends - qualified_dividends) -
						ira_deduction -
						student_loan_interest)


##### Yes: easy to match operators with operands

	income = (gross_wages
						+ taxable_interest
						+ (dividends - qualified_dividends)
						- ira_deduction
						- student_loan_interest)

----
### Imports
##### No:

    import sys, os

##### Yes:

    import os
    import sys

##### Bad:

    import <module> from *

##### Absolute imports are recommended

    import mypkg.sibling
    from mypkg import silbing
    from mypkg.sibling import example

##### Explicit relative imports are acceptable

    from . import sibling
    from .sibling import example

##### Import a class from a class-containing module

    from myclass import MyClass
    from foo.bar.yourclass import YourClass

##### Local name clashes

    import myclass
    import foo.bar.yourclass

    And use "myclass.MyClass" or "foo.bar.yourclass.YourClass"


----
### Module level dunder names
Module level "dunder" names with two leading and two trailing underscores, such as `__all__`, `__author__`, `__version__`, etc

##### Yes:

    """This is the example module.

    This module does stuff.
    """

    from __future__ import barry_as_FLUFL

    __all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Cardinal Biggles'

    import os
    import sys


----
### Whitespace in Expressions and Statements

##### No:

    spam( ham[ 1 ], { eggs: 2 } )

##### Yes:

    spam(ham[1], {eggs: 2})

--

##### No:

    if x == 4 : print x , y ; x , y = y , x

##### Yes:

    if x == 4; print x, y; x, y = y, x

--

##### No:

    ham[lower + offset:upper + offset]
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[lower : : upper]
    ham[ : upper ]

##### Yes:

    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lowser:pper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : setp_fn(x)], ham[:: setp_fn(x)]
    ham[lower + offset : upper + offset]
--

##### No:

    spam (1)

##### Yes:

    spam(1)

--

##### No:

    dct ['key'] = lst [index]

##### Yes:

    dct['key'] = lst[index]

--

##### No:

    x             = 1
    y             = 2
    long_variable = 3

##### Yes:

    x = 1
    y = 2
    long_variable = 3

----
### Other Recommendations

##### No:

		i=i+1
		submitted +=1
		x = x * 2 - 1
		hypot2 = x * x + y * y
		c = (a + b) * (a - b)

##### Yes:

		i = i + 1
		submitted += 1
		x = x*2 - 1
		hypot2 = x*x + y*y
		c = (a+b) * (a-b)


--

##### No:

		def complex(real, imag = 0.0):
				return magic(r = real, i = imag)

##### Yes:

		def complex(real, imag=0.0):
				return magic(r=real, i=imag)

--

##### No:

		def munge(input:AnyStr): ...
		def munge()->PosInt: ...

##### Yes:

		def munge(input: AnyStr): ...
		def munge() -> AnyStr: ...

--

##### No:

		def munge(input: AnyStr=None): ...
		def munge(input: AnyStr, limit = 1000): ...

##### Yes:

		def munge(sep: AnyStr = None): ...
		def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

--

##### Rather no:

		if foo == 'blah': do_blah_thing()
		do_one(); do_two(); do_three()

##### Yes:

		if foo == 'blah':
				do_blah_thing()
		do_one()
		do_two()
		do_three()

--

##### Definitely No:

		if foo == 'blah': do_blah_thing()
		else: do_non_blah_thing()

		try: something()
		finally: cleanup()

		do_one(); do_two(); do_three(long, argument,
																 list, like, this)

		if foo == 'blah': one(); two(); three()

##### Yes:

		if foo == 'blah': do_blah_thing()
		for x in lst: total += x
		while t < 10: t = delay()

----
### Documentation Strings

##### Yes:

		"""Return a foobang

		Optional plotz says to frobnicate the bizbaz first.
		"""

----
### Programming Recommendations

--

##### No:

		if not foo is None:

##### Yes:

		if foo is not None:

--

##### No:

		f = lambda x: 2*x

##### Yes:

		def f(x): return 2*x

--

##### No:

		try:
				# Too broad!
        return handle_value(collection[key])
    expect KeyError:
        # Will also catch KeyError raised by handle_value()
        return key_not_found(key)

##### Yes:

    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)

--

##### No:

    with conn:
        do_stuff_in_transaction(conn)

##### Yes:

    with conn.begin_transaction():
        do_stuff_in_transaction(conn)

--

##### No:

    def foo(x):
        fi x >= 0:
            return math.sqrt(x)

    def bar(x):
        if x < 0:
            return
        return math.sqrt(x)

##### Yes:

    def foo(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return None

    def bar(x):
        if x < 0:
            return None
        return math.sqrt(x)

--

##### No:

    if foo[:3] == 'bar':

##### Yes:

    if foo.startwith('bar'):

--

##### No:

    if type(obj) is type(1):

##### Yes:

    if isinstance(obj, int):

--

##### No:

    if len(seq):
    if not len(seq):

##### Yes:

    if not seq:
    if seq:

--

##### No:

		if greeting == True:


##### Yes:

		if greeting:


##### Worse:

		if greeting is True:
