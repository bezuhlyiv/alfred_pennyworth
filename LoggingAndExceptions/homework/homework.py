import logging
import time
from logging.handlers import RotatingFileHandler

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    max_visitors = 200
    min_visitors = 10

    def __init__(self, visitors_num):
        if visitors_num > self.max_visitors:
            raise TooManyVisitors
        if visitors_num < self.min_visitors:
            raise TooFewVisitors


def make_concert(visitor_num):
    print(f"This concert is going to attend {visitor_num} people.")
    time.sleep(1.5)
    print("Checking if it is possible to organize...")
    time.sleep(1)
    for letter in ".............":
        print(letter, end=' ')
        time.sleep(.25)
    print("\t")
    try:
        Concert(visitor_num)
    except TooManyVisitors:
        logging.warning(f"Number of visitors is more than it can handle: {Concert.max_visitors}!")
        return print("Sorry but you have to reduce number of visitors.")
    except TooFewVisitors:
        logging.warning(f"You need to choose number of visitors bigger than {Concert.min_visitors}")
        return print("Sorry but you need to add more visitors.")
    else:
        return print("The concert will take place.")


logger_object = logging.getLogger("New Logger")
logger_object.setLevel(logging.DEBUG)
handler = RotatingFileHandler("test.log", mode="w")
logger_object.addHandler(handler)


def log_message(message, level):
    if level == 10:
        return logger_object.debug(message)
    elif level == 20:
        logger_object.debug(message)
    elif level == 30:
        return logger_object.warning(message)
    elif level == 40:
        return logger_object.error(message)
    elif level == 50:
        return logger_object.critical(message)
