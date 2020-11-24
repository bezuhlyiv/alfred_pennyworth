import logging.handlers

"""TASK #1"""


def double_result(func):
    def real_double_result(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return real_double_result


def add(a, b):
    return a + b


print(f"__________TASK #1__________:\n\nTest: 1 + 2 = {add(1, 2)}")


@double_result
def add(a, b):
    return a + b


print(f"After multiplying the result of 1 + 2 by 2 the result is: {add(1, 2)}\n")

"""TASK #2"""


def only_even_parameters(func):
    def check_even_numbers(*args):
        for numbers in args:
            if numbers % 2 != 0:
                raise ValueError("Please only use even numbers!")
            else:
                return func(*args)

    return check_even_numbers


@only_even_parameters
def add(a, b):
    return a + b


try:
    print(f"______________TASK #2_______________\n\nThe result of 2 + 2 is \n==>{add(2, 2)}\n")
    print(f"The result of 1 + 2:\n==>{add(1, 2)}\n")
except ValueError as e:
    print(e)


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e

try:
    print(f"ANOTHER TEST:\n\nResult of 1 * 2 * 2 * 2 * 2 is\n{multiply(1, 2, 2, 2, 2)}\n")
except ValueError as e:
    print(e)
"""TASK #3"""

logger = logging.getLogger("Logging args and returns")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


def logged(func):
    def logging_args(*args, **kwargs):
        logger.info(f"_______________TASK #3_______________\n\nTHIS IS A LOG\n===================\nArguments: {args} "
                    f"\nKeyword Arguments: {kwargs} \n"
                    f"Result of a function: {func(*args)}\n===================\n____________________________________")
        return func(*args)

    return logging_args


@logged
def funky(*args):
    return 5 + len(args)


funky(4, 4, 4)

"""TASK #4"""
print("_____________TASK #4______________")


def type_check(correct_type):
    def decorator_args(func):
        def wrapper(num):
            if correct_type != type(num):
                raise ValueError("Bad Type")
            else:
                return func(num)

        return wrapper

    return decorator_args


@type_check(int)
def times2(num):
    return num * 2


try:
    print(times2(2))
    times2('Not A Number')  # "Bad Type" should be printed, since non-int passed to decorated function
except ValueError as e:
    print(e)


@type_check(str)
def first_letter(word):
    return word[0]


try:
    print(first_letter('Hello World'))
    first_letter(['Not', 'A', 'String'])  # "Bad Type" should be printed, since non-str passed to decorated function
except ValueError as e:
    print(e)