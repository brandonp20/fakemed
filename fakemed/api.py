from core_objects import Patient
from utils import export_to_csv
import random

def generate_and_export_patients(
        total_patients: int,
        output_csv_path: str,
        male_percentage: float = 0.5,
        min_age: int = 0,
        max_age: int = 0,
        dob_format: str = None
    ):
    
    if not (0.0 <= male_percentage <= 1.0):
        raise ValueError("male_percentage must be between 0.0 and 1.0")
    
    num_male = int(total_patients * male_percentage)
    num_female = int(total_patients - num_male)

    patient_objects = []
    
    for i in range(num_male):
        p = Patient(sex_param='m', min_age=min_age, max_age=max_age, dob_format=dob_format)
        
        """
        if include_xrays and random.choice([True, True, False]):
            p.add_xray_study(random.choice(['chest', 'abdominal', 'pediatric', 'extremity', None]))
        if include_diagnoses and random.choice([True, True, False]):
            p.add_icd10_diagnosis()
        if include_procedures and random.choice([True, True, False]):
            p.add_cpt_code()
        if include_hl7:
            p.generate_hl7_message(random.choice(['adt', 'orm', None]))
        """
        patient_objects.append(p)
    
    for i in range(num_female):
        p = Patient(sex_param='m', min_age=min_age, max_age=max_age, dob_format=dob_format)
        # if include_xrays and random.choice([True, True, False]):
        #     p.add_xray_study(random.choice(['chest', 'abdominal', 'pediatric', 'extremity', None]))
        # if include_diagnoses and random.choice([True, True, False]):
        #     p.add_icd10_diagnosis()
        # if include_procedures and random.choice([True, True, False]):
        #     p.add_cpt_code()
        # if include_hl7:
        #     p.generate_hl7_message(random.choice(['adt', 'orm', None]))
        patient_objects.append(p)

    patient_data_list = [patient.to_dict_for_csv() for patient in patient_objects]

    if patient_data_list:
        field_names = [
            'patient_id', 'first_name', 'last_name', 'dob', 'age', 'sex', 'ssn', 
            'phone_number', 'address_street', 'address_city', 'address_state', 'address_zip', 
            'xray_1_type', 'xray_1_interpretation', 
            'icd10_codes', 'cpt_codes', 
            'hl7_1_type'
        ]

        processed_patient_data_list = []
        for p_dict in patient_data_list:
            processed_dict = {field: p_dict.get(field) for field in field_names}
            processed_patient_data_list.append(processed_dict)

        export_to_csv(processed_patient_data_list, output_csv_path, fieldnames=field_names)
    else:
        print("No patient data generated to export.")

    return output_csv_path

generate_and_export_patients(50, 'fm-test')