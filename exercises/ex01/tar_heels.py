"""An exercise in remainders and boolean logic."""

__author__ = "730335272"


# Begin your solution here...

x: int = int(input("Enter an int:"))
tar: int = int(x % 2)
heels: int = int(x % 7)

if (tar == 0) or (heels == 0):
    if (tar == 0) and (heels == 0):
        print("TAR HEELS")
    else:
        if (tar == 0):
            print("TAR")
        else: 
            print("HEELS")
else:
    print("CAROLINA")
