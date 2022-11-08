from datetime import date

def how_many_days_lived():

   birth_date = date(2001, 2, 1)
   chosen_date = date(2022, 8, 11)
   result = chosen_date - birth_date
   print("I lived", result.days * 1440, "minutes")

how_many_days_lived()