""" Exercises to practice building generators"""
from collections.abc import Sequence, Generator
from typing import Any

# Up til now, we have always written functions that perform some computation
# and returned a value or tuple of values. This works in many situations, but
# what if we have some large, maybe infinite, computation to complete, but we
# also only require parts of it at a time? That's where **generators** come in.

# Generators are like functions, but instead of **return**ing a value or tuple of
# values, they **yield** values one at a time. We're going to start playing with
# generators by rewriting our Fibonacci function to produce a stream of Fibonacci
# numbers instead of finding the n-th one.

def fib(stop: int|None = None) -> int:
    """Generate a stream of Fibonacci numbers. """
    f2 = 0
    print(f2)
    f1 = 1
    print(f1)
    n = 1
    while stop is None or n < stop:
        f = f2 + f1
        print(f)
        f2, f1 = f1, f
        n += 1


def powers_of(n: int) -> Generator[int]:
    """Generate a stream of powers of n"""
    yield n

        
def chain(*sequences: Sequence[Any]) -> Generator[Any]:
    """Generate a single, ordered stream of items from any number of sequences"""
    yield 0

    
def pairs(items: Sequence[Any]) -> Generator[tuple[Any, Any]]:
    """Generate each unique pair of items. Raises a ValueError if provided with less than two items."""
    yield (0, 1)


def flatten(nested: Sequence[Sequence | Any]) -> Generator[Any]:
    """Generaate a stream of items from the nested sequence in the order they appear"""
    # Hint: each time you come across a Sequence, `yield from flatten(subsequence)`
    #       use `isinstance` to determine if something is a Sequence


if __name__ == "__main__":
    fib(10)
    # should produce 0 1 1 2 3 5 8 13 21 34 55
    # Replace the print function calls with `yield` to create a generator!
    #
    # for x in fib(10):
    #     print(x)
    #
    # should produce the same result
    #
    # Now implement the other functions and test them here
