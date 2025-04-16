import random as rand
import datetime as date
from data.names_data import male_names, female_names, last_names

def first_name(sex=None):
    if sex == None:
        return rand.choice(male_names + female_names)

    if sex is not None: 
        sex = sex.lower()

        if sex == 'm':
            return rand.choice(male_names)
        elif sex == 'f':
            return rand.choice(female_names)
        else:
            raise ValueError("Sex must be 'm', 'f', or None")
    
    else:
        raise ValueError("Sex must be 'm', 'f', or None")

def last_name():
    return rand.choice(last_names)

def full_name(sex=None):
    if sex is not None: 
        sex = sex.lower()
    first = first_name(sex)
    last = last_name()
    return first + ' ' + last

def dob(min_age=0, max_age=120, format=None):
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

def phone_number():
    area_code = rand.randint(100, 999)
    central_office_code = rand.randint(100, 999)
    line_number = rand.randint(1000, 9999)
    return f"({area_code}){central_office_code}-{line_number}"

def ssn():
    area_number = rand.randint(100, 999)
    group_number = rand.randint(10, 99)
    serial_number = rand.randint(1000, 9999)
    return f"{area_number}-{group_number}-{serial_number}"

def address(part=None):
    street = str(rand.randint(100, 9999)) + ' ' + rand.choice(['Main St', 'Second St', 'Second Ave', 'Third St', 'Fourth St', 'Fifth St'])
    city = rand.choice(['Anytown', 'Othertown', 'Sometown'])
    state = rand.choice(['CA', 'TX', 'NY', 'FL', 'IL', 'AZ', 'OR', 'WA', 'CO', 'MA'])
    zip_code = rand.randint(10000, 99999)

    if part == 'street':
        return street
    elif part == 'city':
        return city
    elif part == 'state':
        return state
    elif part == 'zip':
        return zip_code
    elif part is None:
        return f"{street}, {city}, {state} {zip_code}"
    else:
        raise ValueError("Invalid part. Use 'street', 'city', 'state', 'zip_code', or None.")

def sex():
    return rand.choice(['m', 'f'])
