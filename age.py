import datetime as dt
birth_date = input('Please input your date of birth (DD-MM-YYYY): ')
day, month, year = map(int, birth_date.split("-"))
# print(year, month, day)
birth_date_datetime = dt.datetime(year, month, day)
# print(birth_date_datetime)
current_date = dt.datetime.today()
# print(current_date)

# isolate years from variables
delta_years = current_date.year - birth_date_datetime.year
# print(delta_years)

# check if birthday has passed in current year


def calc_age():
    age = 0
    if (birth_date_datetime.month, birth_date_datetime.day) > (current_date.month, current_date.day):
        age = delta_years - 1
    elif (birth_date_datetime.month, birth_date_datetime.day) <= (current_date.month, current_date.day):
        age = delta_years
    return age


age = calc_age()
print(f'Your age is {age}')
