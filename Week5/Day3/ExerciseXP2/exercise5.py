from datetime import date

def how_many_days_left():
    today_date = date(2022, 8, 11)
    chosen_date = date(2023, 1, 1)
    result = chosen_date - today_date
    print(result.days, "days left")
how_many_days_left()
