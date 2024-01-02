# How many days have you already lived
# how_old_are_you_now = input("Please when you born in view dd.mm.yy")
how_old_are_you_now = "27.02.1989"
print(type(how_old_are_you_now))

current_date = "29.12.2023"
sliced_date = current_date.split('.')

sliced_age = how_old_are_you_now.split('.')
print(sliced_age)

current_year = int(sliced_date[2])
lived_years_in_total = current_year - int(sliced_age[2])
print(lived_years_in_total)

lived_months = 