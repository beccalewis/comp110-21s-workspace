"""Tar Heels exercise redux as a structured program."""

__author__ = "730335272"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(x: int) -> str:
    """Tar Heels function."""
    tar: int = int(x % 2)
    heels: int = int(x % 7)

    if (tar == 0) or (heels == 0):
        if (tar == 0) and (heels == 0):
            return("TAR HEELS")
        else:
            if (tar == 0):
                return("TAR")
            else: 
                return("HEELS")
    else:
        return("CAROLINA")


if __name__ == "__main__":
    main()