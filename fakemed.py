import random as rand
from names_data import male_names, female_names, last_names
import datetime as date

male_name_number = len(male_names)
female_name_number = len(female_names)

def get_first_name(sex=''):
    if sex == '':
        return rand.choice(male_names + female_names)

    elif sex == 'M':
        return rand.choice(male_names)

    elif sex == 'F':
        return rand.choice(female_names)
    else:
        raise ValueError("Sex must be 'M', 'F', or ''")

    
def get_last_name():
    return rand.choice(last_names)


def get_full_name(sex=''):
    first = get_first_name(sex)
    last = get_last_name()
    return first + ' ' + last


def get_dob(min_age=0, max_age=120, format=None):
    current_year = date.datetime.now().year
    year = rand.randint(current_year - max_age, current_year - min_age)
    month = rand.randint(1, 12)
    if month == 2:
        day = rand.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = rand.randint(1, 30)
    else:
        day = rand.randint(1, 31)

    if format == None or format == 'y-m-d':
        return f"{year}-{month:02d}-{day:02d}"
    elif format == 'm/d/y':
        return f"{month:02d}/{day:02d}/{year}"
    elif format == 'y/m/d':
        return f"{year}/{month:02d}/{day}"
    elif format == 'd/m/y':
        return f"{day:02d}/{month:02d}/{year}"
    else:
        raise ValueError("Invalid format. Use 'd/m/y', 'm/d/y', 'y/m/d', or 'y-m-d'.")


def get_patient_profile(sex='', min_age=0, max_age=120, format=None):
    first = get_first_name(sex)
    last = get_last_name()
    dob = get_dob(min_age, max_age, format)
    patient_data = {'first_name': first,
                    'last_name': last,
                    'dob': dob
                    }
    return patient_data

print(get_patient_profile('F', 18, 25))