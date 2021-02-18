"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730335272"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")
x: int = int(randint(1, 100))
if x < 50:
    if x < 15:
        print("Someone you know will get COVID.")
    else:
        print("One day, you will die.")
else: 
    if x < 75:
        print("The sun will rise tomorrow.")
    else:
        print("Soon, you will drink water.")

print("Now, go spread positive vibes!")