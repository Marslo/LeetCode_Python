# leetcode_python
My Leetcode source code. Python version.

## [PEP8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

======
### Indentation

#### Yes:

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

#### No:

    # Arguments on first line forbidden when not using vertical alignment.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

    # Further indentation required as indentation is not distinguishable.
    def long_function_name(
        var_one, var_two, var_three,
        var_four):
        print(var_one)

#### Optional:

    # Hanging indents *may* be indented to other than 4 spaces.
    foo = long_function_name(
      var_one, var_two,
      var_three, var_four)

#### If-statemant

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

#### List

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


======
### Maximum Line Length

#### Yes:
		with open('/path/to/some/file/you/want/to/read') as file_1, \
				 open('/path/to/some/file/being/written', 'w') as file_2:
				file_2.write(file_1.read())

======
### Should a Line break before or after a binary operator?
#### No: operators sit far away from their operands

	income = (gross_wages +
						taxable_interest +
						(dividends - qualified_dividends) -
						ira_deduction -
						student_loan_interest)


#### Yes: easy to match operators with operands

	income = (gross_wages
						+ taxable_interest
						+ (dividends - qualified_dividends)
						- ira_deduction
						- student_loan_interest)
