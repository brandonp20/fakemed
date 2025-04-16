import random as rand
from names_data import male_names, female_names, last_names
from radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from hl7_data import facilities, hl7_apps
import datetime as date

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
    first = get_first_name(sex)
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

def generate_patient(pt_sex=None, min_age=0, max_age=120, format=None):
    if pt_sex is None:
        pt_sex = sex()
        
    patient_data = {'first_name': first_name(pt_sex),
                    'last_name': last_name(),
                    'sex': pt_sex,                    
                    'dob': dob(min_age, max_age, format),
                    'ssn': ssn(),
                    'phone_number': phone_number(),

                    # 'xray_interp': get_xray(xray_type=None),
                    # 'hl7_message': get_hl7_message(msg_type=None),
                    }
                    
    return patient_data


### Additional Information
def get_xray(xray_type=None):
    if xray_type is None:
        return rand.choice(chest_xray_interpretations + abdominal_xray_interpretations + spinal_xray_interpretations + extremity_xray_interpretations + pediatric_xray_interpretations + miscellaneous_xray_interpretations)

    else:
        xray_type = xray_type.lower()
        if xray_type == 'chest':
            return rand.choice(chest_xray_interpretations)
        elif xray_type == 'abdominal':
            return rand.choice(abdominal_xray_interpretations)
        elif xray_type == 'spinal':
            return rand.choice(spinal_xray_interpretations)
        elif xray_type == 'extremity':
            return rand.choice(extremity_xray_interpretations)
        elif xray_type == 'pediatric':
            return rand.choice(pediatric_xray_interpretations)
        elif xray_type == 'miscellaneous':
            return rand.choice(miscellaneous_xray_interpretations)
        else:
            raise ValueError("Invalid type. Use 'chest', 'abdominal', 'spinal', 'extremity', 'pediatric', or 'miscellaneous'.")

def get_hl7_message(msg_type=None):
    if msg_type == None:
        msg_type = rand.choice(['adt', 'orm', 'dft'])

    if msg_type == 'adt': 
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||ORM^O01|1234567890|P|2.3"
        PID = f"PID|1||123456^^^Hospital^MR||{rand.choice(last_names)}^{rand.choice(male_names + female_names)}^^^||{dob()}|{sex()}|||{address('street')}^^{address('city')}^{address('state')}^{address('zip')}||{phone_number()}|||||||"
        PV1 = f"PV1|1|{rand.choice(['I', 'O', 'E'])}|Floor^Room^Bed|U|A0||||{rand.randint(100000000, 999999999)}^^{rand.choice(male_names + female_names)}^^^Dr.|||||||||||||||202310031200"
        ORC = f"ORC|NW|1234567890||||||202310031200|||A0"
        OBR = f"OBR|1|1234567890|9876543210^Radiology^L|||202310031200|||||||||||||||202310031200|||||||F|||||||"
        OBX = f"OBX|1|{address('state')}|12345^Radiology Report^L||No acute cardiopulmonary process identified. Heart size within normal limits. Lungs are clear.|||F|||202310031200"
        hl7_message = "\n".join([MSH, PID, PV1, ORC, OBR, OBX])

    elif msg_type == 'orm':
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||ORM^O01|1234567890|P|2.3"
        PID = "PID|1||123456^^^Hospital^MR||Doe^John^^^Mr.||19800101|M|||123 Main St^^Anytown^CA^12345||(555)555-5555|||||||"
        ORC = "ORC|NW|1234567890||||||202310031200|||A0"
        OBR = "OBR|1|1234567890|9876543210^Radiology^L|||202310031200|||||||||||||||202310031200|||||||F|||||||"
        hl7_message = "\n".join([MSH, PID, ORC, OBR])
    elif msg_type == 'dft':
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||DFT^P03|1234567890|P|2.3"
        PID = "PID|1||123456^^^Hospital^MR||Doe^John^^^Mr.||19800101|M|||123 Main St^^Anytown^CA^12345||(555)555-5555|||||||"
        FT1 = "FT1|1|1234567890||||202310031200|||A0|||||||"
        PV1 = "PV1|1|I|Ward^Room^Bed|U|A0||||1234^Smith^John^^^Dr.|||||||||||||||202310031200"
        IN1 = "IN1|1|123456^^^Insurance^ID||Doe^John^^^Mr.|||||||||||||||202310031200"
        hl7_message = "\n".join([MSH, PID, FT1])
    
    return hl7_message

print(generate_patient())