"""
Stronghold Kingdoms uses Greenwich Mean Time, so all calculations
must consider this to accurately determine the time of the next AI attack
"""
import datetime
import math
from datetime import timedelta

now = datetime.datetime.now()
now_string = now.strftime("%m/%d/%y @ %H:%M")

"""
This code will calculate the time until the next snake attack
"""
initial_wolf_date = datetime.datetime(year = 2022, month = 4, day = 11, hour = 16, minute = 33)
initial_wolf_date_string = initial_wolf_date.strftime("%m/%d/%y @ %H:%M")

difference_wolf = now - initial_wolf_date
difference_wolf_hours = difference_wolf.days * 24 + difference_wolf.seconds // 3600
wolf_ratio = difference_wolf_hours / 35 + 1

updated_wolf_date = initial_wolf_date + datetime.timedelta(hours=(35 * math.floor(wolf_ratio)))
updated_wolf_date_string = updated_wolf_date.strftime("%m/%d/%y @ %I:%M %p")

print("The next wolf attack will be at: ", updated_wolf_date_string)

"""
This code will calculate the time until the next pig attack
"""
initial_pig_date = datetime.datetime(year = 2022, month = 3, day = 25, hour = 2, minute = 59)
initial_pig_date_string = initial_wolf_date.strftime("%m/%d/%y @ %H:%M")

difference_pig = now - initial_pig_date
difference_pig_hours = difference_pig.days * 24 + difference_pig.seconds // 3600
pig_ratio = difference_pig_hours / 88 + 1

updated_pig_date = initial_pig_date + datetime.timedelta(hours=(88 * math.floor(pig_ratio)))
updated_pig_data_string = updated_pig_date.strftime("%m/%d/%y @ %I:%M %p")

print("The next pig attack will be at: ", updated_pig_data_string)
print("Reminder to not get tburged")
