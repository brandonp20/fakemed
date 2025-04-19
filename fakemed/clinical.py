import random as rand
from data.radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from data.names_data import male_names, female_names, last_names
from utils import _load_icd10_codes_to_memory, _load_cpt_codes_to_memory

_cached_icd10_codes = None
_cached_cpt_codes = None

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

def icd10():
    """Returns a random ICD-10 code."""
    global _cached_icd10_codes
    if _cached_icd10_codes is None:
        _cached_icd10_codes = _load_icd10_codes_to_memory()

    if not _cached_icd10_codes:
        return "Error: No ICD-10 codes loaded or loading failed."

    return rand.choice(_cached_icd10_codes)

def cpt():
    """Returns a random CPT code."""
    global _cached_cpt_codes
    if _cached_cpt_codes is None:
        _cached_cpt_codes = _load_cpt_codes_to_memory()

    if not _cached_cpt_codes:
        return "Error: No CPT codes loaded or loading failed."

    return rand.choice(_cached_cpt_codes)
