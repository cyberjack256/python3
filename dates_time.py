from datetime import datetime
# Dealing with months
current_month = datetime.now().strftime('%m') # 02 # padded
current_month_text = datetime.now().strftime('%h') # Dec0
current_month_text = datetime.now().strftime('%B') # December

# Dealing with days
current_day = datetime.now().strftime('%d')   # 23 padded
current_day_text = datetime.now().strftime('%a')  # Wed
current_day_full_text = datetime.now().strftime('%A')  # Wednesday
current_weekday_day_of_today = datetime.now().strftime('%w') # Where 0 is Sunday and 6 is Saturday.

# Dealing with years
current_year_full = datetime.now().strftime('%Y')  # 2022
current_year_short = datetime.now().strftime('%y')  # 22 without century

# Dealing with seconds, minutes, hours
current_second= datetime.now().strftime('%S') # 24
current_minute = datetime.now().strftime('%M') # 23
current_hour = datetime.now().strftime('%H') # 18 -> 6pm
current_hour = datetime.now().strftime('%I') # 04 pm
current_hour_am_pm = datetime.now().strftime('%p') # 4 pm
current_microseconds = datetime.now().strftime('%f') # 623596

# Dealing with timezones
current_timezone = datetime.now().strftime('%Z') # UTC, EST, CST etc. (empty string if the object is not aware; purely up to the program).