import random as rand
import csv
from data.radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from data.names_data import male_names, female_names, last_names

def xray(xray_type=None):
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

def icd_10s():
    icd_10s = []
    with open('data/icd_10s.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            icd_10s.append(row[0])
    return rand.choice(icd_10s)