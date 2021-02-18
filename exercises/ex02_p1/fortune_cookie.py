"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730335272"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Fortune cookie contents!"""
    x: int = int(randint(1, 100))
    if x < 50:
        if x < 15:
            return("Someone you know will get COVID.")
        else:
            return("One day, you will die.")
    else: 
        if x < 75:
            return("The sun will rise tomorrow.")
        else:   
            return("Soon, you will drink water.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()