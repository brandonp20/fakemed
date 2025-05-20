import datetime as date
import csv
import random as rand
# from .data.hl7_data import facilities, hl7_apps
from .utils import load_male_names, load_female_names, load_last_names, export_to_csv
from .data.radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from .personal import first_name, last_name as generate_last_name_personal, dob, sex, phone_number, ssn # Renamed last_name
from .clinical import xray, icd10, cpt
from .connectivity import hl7_message

import uuid

male_names = load_male_names()
female_names = load_female_names()
last_names = load_last_names()

class Demographics:
    def __init__(self, sex_param=None, min_age=0, max_age=120, dob_format=None):
        self.sex = self._generate_sex(sex_param)
        self.first_name = self._generate_first_name()
        self.last_name = self._generate_last_name()
        self.middle_name = self._generate_middle_name()
        self.dob = self._generate_dob(min_age, max_age, dob_format)
        self.ssn = self._generate_ssn()
        self.phone_number = self._generate_phone_number()
        self.address_number, self.address_street, self.address_city, self.address_state, self.address_zip = self._generate_address_parts()
        
    def _generate_sex(self, sex_param=None):
        if sex_param is None:
            return rand.choice(['m', 'f'])
        sex_param = sex_param.lower()
        if sex_param in ['m', 'f']:
            return sex_param
        raise ValueError("Sex must be 'm', 'f', or None")
    
    def _generate_first_name(self):
        if self.sex == 'm':
            return rand.choice(male_names)
        else: 
            return rand.choice(female_names)
        
    def _generate_last_name(self):
        return rand.choice(last_names)
    
    def _generate_middle_name(self):
        if self.sex == 'm':
            return rand.choice(male_names)
        else: 
            return rand.choice(female_names)
    
    def _get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def _generate_dob(self, min_age=0, max_age=120, format_param=None):
        current_year = date.datetime.now().year
        year = rand.randint(current_year - max_age, current_year - min_age)
        month = rand.randint(1,12)
        day = rand.randint(1, 28)
        if month == 2:
            day = rand.randint(1, 28)
        elif month in [4, 6, 9, 11]:
            day = rand.randint(1, 30)
        else:
            day = rand.randint(1, 31)

        if format_param is None or format_param == 'y-m-d': 
            return f"{year}-{month:02d}-{day:02d}" 
        elif format_param == 'm/d/y': 
            return f"{month:02d}/{day:02d}/{year}"

    def _generate_phone_number(self): 
        return f"({rand.randint(100, 999)}) {rand.randint(100, 999)}-{rand.randint(1000, 9999)}" 

    def _generate_ssn(self): 
        return f"{rand.randint(100, 999)}-{rand.randint(10, 99)}-{rand.randint(1000, 9999)}"

    def _generate_address_parts(self): 
        number = rand.randint(100, 9999)
        street = {rand.choice(['Main St', 'Second St', 'Oak Ave'])}
        city = rand.choice(['Anytown', 'Othertown', 'Sometown']) 
        state = rand.choice(['CA', 'TX', 'NY', 'FL', 'IL']) 
        zip_code = rand.randint(10000, 99999) 
        return number, street, city, state, str(zip_code) 
    
    def get_address_string(self): 
        return f"{self.address_number}, {self.address_street}, {self.address_city}, {self.address_state} {self.address_zip}" 
    
    def __str__(self): 
        return f"{self._get_full_name()}, DOB: {self.dob}, Sex: {self.sex.upper()}"

class Patient:
    def __init__(self, sex_param=None, min_age=0, max_age=120, dob_format=None):
        self.patient_id = str(uuid.uuid4())
        self.demographics = Demographics(sex_param=sex_param, min_age=min_age, max_age=max_age, dob_format=None)
    
    def _calculate_age(self): 
        # Calculates age based on DOB 
        if not self.demographics.dob: 
            return None 
        try: # Assuming DOB is 'YYYY-MM-DD' or can be parsed 
            dob_date = date.datetime.strptime(self.demographics.dob.split(' ')[0], '%Y-%m-%d').date() 
            # Handle potential time part 
            today = date.date.today() 
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day)) 
            return age 
        
        except ValueError: # If DOB format is different or invalid 
            return None

    def to_dict_for_csv(self): 
        """Converts patient data to a flat dictionary for CSV export.""" 
        age = self._calculate_age() 
        data = { 
            'patient_id': self.patient_id, 
            'first_name': self.demographics.first_name, 
            'last_name': self.demographics.last_name, 
            'dob': self.demographics.dob, 
            'age': age, 
            'sex': self.demographics.sex.upper() if self.demographics.sex else None, 
            'ssn': self.demographics.ssn, 
            'phone_number': self.demographics.phone_number, 
            'address_street': self.demographics.address_street, 
            'address_city': self.demographics.address_city, 
            'address_state': self.demographics.address_state, 
            'address_zip': self.demographics.address_zip
        }

        return data

demo = Patient()

print(demo)
