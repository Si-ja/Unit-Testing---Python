# Unit Testing in Python

This repository is dedicated to tackling in a brief way 
of what are unit tests and how they can be really helpful 
to any ongoing projects you might partake in (now only 
with Python, but in programming in general).

## Concepts

Unit testing is as simple of an idea as:
> Creating a number of tests, that assess the performance of the 
>developed code solution.

Writing multiple test cases could be time consuming 
initially. However, the benefit of this:
* You do not need to test a number of multiple scenarios
on how your code handles them by hand.
* If you update your code solution - in a lot of cases
you want to make sure nothing has been broken in how
the code used to work and re-using previous test cases
could be a huge time saver.

## Practical example

To understand the practical usage of unit testing, 
consider the following scenario. You have created a class
in a package `Checker.Tools` that has only 1 method:
`binary`. The idea behind this class and method is that
one can pass 2 lists into it, and will get information
on which particular values differ per two lists.

Couple of conditions are set:
* It is considered that only 2 lists are compared.
* Lists can be either native python lists or numpy 
arrays.
* It is considered that the user would only put in 
for checking 1 dimensional arrays or lists (i.e. no
nested lists are considered).
* Values are compared to the biggest lists (i.e. 
if one list is [1, 2] and the second is [1, 2, 3] then
the answer of the method would be [True, True, False]
meaning that the first two values in both lists match,
but the third value that is present only in the second 
list is considered to not match).

You create the code and create a unit testing file:
`test_Tools.py`. Your method can be considered fully
functional if all of the tests ran in the said file
are successful.

__BUT!__ 

Now you have been approached and told that though your
class works well - there are concerns that errors will
be given to a user if they pass nested or more than 1
dimensional lists and/or arrays to the method for checking.
The main issue is that the errors will be not informative,
as they are not developed by us, but just some issues
python would run into while using our function for processing
the non-intended data input.

To address this - you are asked to create custom errors
that would be thrown to the user if such condition takes
place, explaining what is the current issue with their
actions in specific details.

As a rule - you would update the previously created  
`Checker.Tools` file. For this case to allow for
demonstration of changes happening - a second file is
created in the same location called `Checker.ToolsUpdate`.
You add the following piece of code to your file:

```python
import numpy as np
if(isinstance(a, np.ndarray) or isinstance(b, np.ndarray)):
    if a.ndim > 1 or b.ndim > 1:
        raise ValueError("This method only processes 1 dimensional arrays")
else:
    if any(isinstance(i, list) for i in a) or any(isinstance(i, list) for i in b):
        raise ValueError("This method only processes 1 dimensional lists")
``` 

It should be enough to direct the user in explaining
what could be wrong if they are passing arrays that the
method has not intended to account for. However, we 
also want to make sure that adding of this code has
not in any way affected our previously developed
codes' performance, especially if it is being used in production 
and alterations to its functionality could break 
crucial processes going already on.

The updated code solution should be only put into 
deployment if the old test cases will be successful
on the run time, meaning old functionalities have not
been broken.

Of course, you can add to the unit testing file more 
conditions, such that check whether the errors pop-up 
as intended. For that a new file has been created for 
this example called `test_ToolsUpdate` and new tests 
have been added to it (for instance):

```python
def test_binaryErrors(self):
    self.assertRaises(ValueError, Functions.binary, [1], [[1], [1, 2]])

def test_binaryErrorsNumpy(self):
    import numpy as np
    self.assertRaises(ValueError, Functions.binary, np.array((1)), np.array([[1, 3], [1, 2]]))
```

## How to write proper tests

There are no set in stone rules for this. In essence
you need to write as many test cases as would be
satisfactory to make sure that the code works fully as
intended. More does not mean better, but rather make
sure that it works for regular and edge cases.

For example, if you have a function that divides
values `a` and `b` - it would be smart to see
if division happens with integer values, floats,
what happens if `a = 0; b = anything; a/b` and if any
intended errors pop-up when `a = anything; b = 0; a/b`.
Several tests should be enough, but this heavily depends
on the scope of your code.

There are multiple types of unit tests that can be found
with the official python documentation:
[Unit testing framework for python](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug).
Such tests can cover verifying whether particular input
allows for the developed code to yield a particular expected output, 
or if any conditions should trigger particular errors.

The field is quite broad and is refered to as `TDD -
Test Driven Developemnt`, where code is developed
in respect to the outcomes for particular inputs it
is expected to bring. 