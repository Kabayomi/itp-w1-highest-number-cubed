"""This is the entry point of the program."""


def highest_number_cubed(limit):
    x = 0
    while x ** 3 <= limit:
        x += 1
        if x ** 3 > limit:
            return x - 1
            
