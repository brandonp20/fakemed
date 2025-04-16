import csv

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
    