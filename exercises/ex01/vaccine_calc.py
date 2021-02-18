"""A vaccination calculator."""

__author__ = "730335272"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Population: "))
doses_done: int = int(input("Doses administered: "))
doses_daily: int = int(input("Doses per day: "))
percent_target: int = int(input("Target percent vaccinated: "))

# the calculation part: variables --> number of days
doses_needed: float = float((2 * (population * (percent_target / 100))) - doses_done)
days_needed: timedelta = timedelta(round(doses_needed / doses_daily))
print(days_needed)

# adding the days needed to today's date
today: datetime = datetime.today()
date_done: datetime = today + days_needed

# output
print("We will reach " + str(percent_target) + "% vaccination in " + str(days_needed.days) + " days, which falls on " + str(date_done.strftime("%B %d, %Y")) + ".")