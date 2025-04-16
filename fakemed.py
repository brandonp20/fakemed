import random as rand
from names_data import male_names, female_names, last_names

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

print(full_name())
