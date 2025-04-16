import random as rand
from names_data import male_names, female_names, last_names
import datetime as date

male_name_number = len(male_names)
female_name_number = len(female_names)

def first_name(sex=''):
    if sex == '':
        return rand.choice(male_names + female_names)

    elif sex == 'M':
        return rand.choice(male_names)

    elif sex == 'F':
        return rand.choice(female_names)
    else:
        raise ValueError("Sex must be 'M', 'F', or ''")

    
def last_name():
    return rand.choice(last_names)

def full_name(sex=''):
    first = first_name(sex)
    last = last_name()
    return first + ' ' + last

def date_of_birth():
    current_year = date.datetime.now().year
    year = rand.randint(current_year - 100, current_year - 1)
    month = rand.randint(1, 12)
    if month == 2:
        day = rand.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = rand.randint(1, 30)
    else:
        day = rand.randint(1, 31)

    return f"{year}-{month:02d}-{day:02d}"

print(full_name())

print(date_of_birth())