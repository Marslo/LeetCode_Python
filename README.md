# leetcode_python
My Leetcode source code. Python version.


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

OR

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
