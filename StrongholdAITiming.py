"""
Stronghold Kingdoms uses Greenwich Mean Time, so all calculations
must consider this to accurately determine the time of the next AI attack
"""
import datetime
import math
from datetime import timedelta

# Program constants
BASE_YEAR = 2022

BASE_WOLF_MONTH = 4
BASE_WOLF_DAY = 11
BASE_WOLF_HOUR = 16
BASE_WOLF_MINUTE = 33

BASE_PIG_MONTH = 3
BASE_PIG_DAY = 25
BASE_PIG_HOUR = 2
BASE_PIG_MINUTE = 59

WOLF_INTERVAL = 35
PIG_INTERVAL = 88
SECONDS_TO_HOUR = 3600
HOURS_TO_DAY = 24

now = datetime.datetime.now()

"""
This code will calculate the time until the next wolf attack
"""
initial_wolf_date = datetime.datetime(year = BASE_YEAR, month = BASE_WOLF_MONTH, day = BASE_WOLF_DAY, hour = BASE_WOLF_HOUR, minute = BASE_WOLF_MINUTE)

difference_wolf = now - initial_wolf_date
difference_wolf_hours = difference_wolf.days * HOURS_TO_DAY + difference_wolf.seconds // SECONDS_TO_HOUR
wolf_ratio = difference_wolf_hours / WOLF_INTERVAL + 1

updated_wolf_date = initial_wolf_date + datetime.timedelta(hours=(WOLF_INTERVAL * math.floor(wolf_ratio)))
updated_wolf_date_string = updated_wolf_date.strftime("%m/%d/%y @ %I:%M %p")

print("The next wolf attack will be at: ", updated_wolf_date_string)

"""
This code will calculate the time until the next pig attack
"""
initial_pig_date = datetime.datetime(year = BASE_YEAR, month = BASE_PIG_MONTH, day = BASE_PIG_DAY, hour = BASE_PIG_HOUR, minute = BASE_PIG_MINUTE)

difference_pig = now - initial_pig_date
difference_pig_hours = difference_pig.days * HOURS_TO_DAY + difference_pig.seconds // SECONDS_TO_HOUR
pig_ratio = difference_pig_hours / 88 + 1

updated_pig_date = initial_pig_date + datetime.timedelta(hours=(PIG_INTERVAL * math.floor(pig_ratio)))
updated_pig_data_string = updated_pig_date.strftime("%m/%d/%y @ %I:%M %p")

print("The next pig attack will be at: ", updated_pig_data_string)
print("Reminder to not get tburged")
