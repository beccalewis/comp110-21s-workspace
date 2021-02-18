"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730335272"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses_done: int = int(input("Doses administered: "))
    doses_daily: int = int(input("Doses per day: "))
    percent_target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_needed: timedelta = timedelta(days_to_target(population, doses_done, doses_daily, percent_target))
    # TODO 4: Call future_date and store result in a variable.
    date_done: str = str(future_date(days_needed))
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(percent_target) + "% vaccination in " + str(days_needed.days) + " days, which falls on " + date_done + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A function calculating days until target."""
    doses_needed: float = float((2 * (population * (target / 100))) - doses)
    days_needed: int = int(round(doses_needed / doses_per_day))
    return(days_needed)


# TODO 3: Define future_date function
def future_date(days_to_target: int) -> str:
    """Finds projected date vaccination goal will be reached."""
    today: datetime = datetime.today()
    date_done: datetime = today + days_to_target
    return str(date_done.strftime("%B %d, %Y"))



if __name__ == "__main__":
    main()
