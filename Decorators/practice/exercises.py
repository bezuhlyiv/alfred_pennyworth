import time
import logging.handlers
import sys


"""Exercise Practice #1"""

TROLL_TAX = 50


class TrollIsAngry(Exception):
    pass


class Person:
    def __init__(self, money):
        self.money = money


def troll(function):
    def wrapper(*args, **kwargs):
        person = args[0]
        if person.money >= TROLL_TAX:
            person.money -= TROLL_TAX
        else:
            raise TrollIsAngry
        return function(*args, **kwargs)

    return wrapper


@troll
def bridge(person: Person):
    print(f"Person passed the bridge with money {person.money}")
    return


if __name__ == "__main__":
    vasya = Person(300)
    bridge(vasya)

"""Exercise Practice #2"""


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{self.func.__name__} ran in: {t2} sec')
        return result


@Timer
def my_func():
    time.sleep(2)


my_func()

"""Exercise #3"""


def decorator(func):
    def wrapper(num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError('number should be positive and int')
        return func(num)

    return wrapper


@decorator
def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num - 1) * num


"""Exercise #4"""


def calc(numb: int):
    lst = []
    for i in range(1, numb + 1):
        a = 0
        while i != a:
            if len(lst) == numb:
                break
            a += 1
            lst.append(i)
    print(lst)


calc(7)

"""Exercise #5"""
total = 0
list1 = [1, -3, 5, -6, -10, 13, 5, -4, 1]
list2 = []


for ele in range(len(list1)):
    print(list1[ele])
    time.sleep(0.7)
    total = total + list1[ele]
    list2.append(list1[ele])
    if total == 0:
        multiplied_list: int = sum([element ** 2 for element in list2])
        print(multiplied_list)
        break


"""Exercise #6"""
logger = logging.getLogger("Message_Log")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class Loggable:
    def log(self, msg):
        log_messages = str(time.ctime()) + ": " + str(msg)
        return log_messages


class LoggableList(Loggable, list):

    def append(self, item):
        super(LoggableList, self).append(item)
        logger.info(f"{super().log(item)}")


log_appends = LoggableList()
log_appends.append(1)


"""Exercise #7"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x: int):
        try:
            if x < 0:
                raise NonPositiveError()
            else:
                super(PositiveList, self).append(x)
        except NonPositiveError:
            print("You should only use positive numbers!")


list_with_positive_numbers = PositiveList()
list_with_positive_numbers.append(4)
