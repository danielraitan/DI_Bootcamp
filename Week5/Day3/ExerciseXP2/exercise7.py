import datetime

today = datetime.datetime.now()
print("todays date and time:", today)

next_holiday = datetime.datetime(2022,12,18,8,15)

final_result = next_holiday - today
print(f"hanukkah is in {final_result} hours")