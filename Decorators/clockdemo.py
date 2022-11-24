import time
from clockdeco import clock
from typing import Union

"""
Look at 'Fluent Python' page 224
"""


@clock
def snooze(seconds: Union[int, float]):
    # delay execution for a number of seconds
    time.sleep(seconds)


@clock
def factorial(n: int):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)  # should output close to 0.123
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)
