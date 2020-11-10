import random


def random_number(min, max):
    return random.randint(min, max)


def random_phone(min_range=70000000111, max_range=70009999999):
    return str(random_number(min_range, max_range))
