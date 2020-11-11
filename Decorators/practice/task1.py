# import time
#
# """First exercise"""
# TROLL_TAX = 50
#
#
# class TrollIsAngry(Exception):
#     pass
#
#
# class Person:
#     def __init__(self, money):
#         self.money = money
#
#
# def troll(function):
#     def wrapper(*args, **kwargs):
#         person = args[0]
#         if person.money >= TROLL_TAX:
#             person.money -= TROLL_TAX
#         else:
#             raise TrollIsAngry
#         return function(*args, **kwargs)
#
#     return wrapper
#
#
# @troll
# def bridge(person: Person):
#     print(f"Person passed the bridge with money {person.money}")
#     return
#
#
# if __name__ == "__main__":
#     vasya = Person(300)
#     bridge(vasya)
#
# """SECOND EXERCISE"""
#
#
# class Timer:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         t1 = time.time()
#         result = self.func(*args, **kwargs)
#         t2 = time.time() - t1
#         print(f'{self.func.__name__} ran in: {t2} sec')
#         return result
#
#
# @Timer
# def my_func():
#     time.sleep(2)
#
#
# my_func()
#
# """EXERCISE 3"""
#
#
# def decorator(func):
#     def wrapper(num):
#         if not isinstance(num, int) and num <= 0:
#             raise ValueError('Number should be positive and int')
#         return func(num)
#
#     return wrapper
#
#
# @decorator
# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return factorial(num - 1) * num
#
#
# """EXERCISE 4"""


def task(number):
    for i in range(1, number + 1):
        numbers_list = []
        x = 0
        while i != x and len(numbers_list) <= number:
            numbers_list.append(x)
        return numbers_list


print(task(4))
