from typing import Any, Callable
import numpy as np
from dis import dis  # disassemble into bytecode


# Look at scopes
# declare global var
y = 2

def f1(x):
    print(x)
    print(y)

def f2(x):
    print(x)
    print(y)  # -> therefore this doesn't load global 'y' from global scope
    y = 3  # variable defined inside function so must be a local var --^


dis(f1)
print("---------------------------------------------")
dis(f2)

# ----------------------------------CLOSURE----------------------------------------------
def make_averager():
    series = []

    def averager(new_val):
        """
        The binding for 'series' is kept in the __closure__ attribute of averager()
        Each item in __closure__ is a cell corresponding to a name in __code__.co_freevars
        A 'Closure' is a function that retains the bindings of the free_vars that exist when the func is defined
        so that they can be used later when the func is invoked and the defining scope is lost
        Only used in nested funcs, like attribtues
        """
        series.append(new_val)  # series is a 'free variable' inside this func
        total = sum(series)
        return total / len(series)

    return averager


class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_val):
        self.series.append(new_val)
        total = sum(self.series)
        return total / len(self.series)


# --------------
# example of broken code
def make_averager_2():
    count = 0
    total = 0

    def averager_2(new_value):
        """
        Broken version:
        """
        nonlocal count, total  # without this, the following breaks
        count += 1  # this is count = count + 1 where count is an immutable type. Without nonlocal, we cannot rebind
        total += new_value
        return total / count
    return averager_2