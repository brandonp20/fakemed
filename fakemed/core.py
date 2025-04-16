import datetime as date
import csv
import random as rand
from data.hl7_data import facilities, hl7_apps
from data.names_data import male_names, female_names, last_names
from data.radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from personal import first_name, last_name, dob, sex, phone_number, ssn
from clinical import xray
from connectivity import hl7_message
from utils import export_to_csv

def generate_patients(count=1, pt_sex=None, min_age=0, max_age=120, format=None):
    patient_list = []
    for n in range(count):
        current_sex = pt_sex
        if current_sex is None:
            current_sex = sex()  
        else:
            current_sex = current_sex.lower()

        patient_data = { # Personal
                        'first_name': first_name(pt_sex),
                        'last_name': last_name(),
                        'sex': current_sex,                    
                        'dob': dob(min_age, max_age, format),
                        'ssn': ssn(),
                        'phone_number': phone_number(),

                        # Clinical
                        'xray_interp': xray(xray_type=None),
                        # 'us_interp': us(us_type=None),
                        # 'ct_interp': ct(ct_type=None),
                        # 'mri_interp': mri(mri_type=None),

                        # Connectivity
                        # 'hl7_message': hl7_message(msg_type=None),
                        }
                        
        patient_list.append(patient_data)

    return patient_list