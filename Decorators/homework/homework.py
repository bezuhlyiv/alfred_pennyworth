import logging.handlers

"""TASK #1"""


def double_result(func):
    def real_double_result(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return real_double_result


@double_result
def add(a, b):
    return a + b


"""TASK #2"""


def only_even_parameters(func):
    def check_even_numbers(*args):
        for numbers in args:
            if numbers % 2 != 0:
                return "Please only use even numbers!"
            else:
                return func(*args)

    return check_even_numbers


@only_even_parameters
def add(a, b):
    return a + b


print(add(2, 2))


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


"""TASK #3"""

logger = logging.getLogger("Logging args and returns")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


def logged(func):
    def logging_args(*args, **kwargs):
        logger.info(f"Arguments: {args} \nKeyword Arguments: {kwargs} \nResult of a function: {func(*args)}")
        return func(*args)

    return logging_args


@logged
def funky(*args):
    return 5 + len(args)


print(funky(4, 4, 4))


"""TASK #4"""


def type_check(correct_type):
    def decorator_args(func):
        def wrapper(num):
            if correct_type != type(num):
                return print("Bad Type")
            else:
                return func(num)

        return wrapper

    return decorator_args


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
