# leetcode_python
My Leetcode source code. Python version.

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
##### Yes:

##### No:
##### Yes:

##### No:
##### Yes:

##### No:
##### Yes:

##### No:
##### Yes:

##### No:
##### Yes:
