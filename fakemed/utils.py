import csv
import os

def export_to_csv(patient_list, filename="patients.csv"):
    if not patient_list:
        print("No patients to export")
        return None
    
    fieldnames = patient_list[0].keys()
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Header row
            writer.writeheader()
            
            # Patient rows
            writer.writerows(patient_list)
            
        return filename
        
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return None


### Data Loading from CSV to Memory
def _load_icd10_codes_to_memory():
    global _ICD10_CODES
    codes = []
    try:
        with open(_ICD10_FILE_PATH, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header row
            for row in reader:
                if row: # Ensure row is not empty
                    codes.append(row[0]) # Adds row to list
    except FileNotFoundError:
        print(f"Error: ICD-10 data file not found at {_ICD10_FILE_PATH}")
        _ICD10_CODES = []
        return
    except Exception as e:
        print(f"Error reading ICD-10 data file: {e}")
        # Still assign to global within utils for potential internal use, but also return
        _ICD10_CODES = []
        return _ICD10_CODES # Return empty list on error

    _ICD10_CODES = codes
    return _ICD10_CODES # Return the loaded codes

# Store codes in memory after first read
_ICD10_CODES = None
_ICD10_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'icd10.csv')

def _load_cpt_codes_to_memory():
    global _CPT_CODES
    codes = []
    try:
        with open(_CPT_FILE_PATH, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header row
            for row in reader:
                if row: # Ensure row is not empty
                    codes.append(row[0]) # Adds row to list
    except FileNotFoundError:
        print(f"Error: CPT data file not found at {_CPT_FILE_PATH}")
        _CPT_CODES = []
        return
    except Exception as e:
        print(f"Error reading CPT data file: {e}")
        # Still assign to global within utils for potential internal use, but also return
        _CPT_CODES = []
        return _CPT_CODES # Return empty list on error

    _CPT_CODES = codes
    return _CPT_CODES # Return the loaded codes

_CPT_CODES = None
_CPT_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'cpt.csv')
