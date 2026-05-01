import csv
import time

# Task 1
outputDictionary = {}

with open('scp_statements.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for i in reader:
        if i['Statement Category'] == 'Myocardial Infarction':
            key = i[reader.fieldnames[0]]
            val = i['description']
            outputDictionary[key] = val
    
# Task 2
def mi_patient_streamer(csv_path, mapping_dict):
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            scp_codes_str = row['scp_codes']
            matches = []

            for code, diagnosis in mapping_dict.items():
                if code in scp_codes_str:
                    matches.append(diagnosis)

            if matches:
                yield {
                    'patient_id': row['patient_id'],
                    'age': row['age'],
                    'sex': row['sex'],
                    'record_date': row['recording_date'],
                    'diagnosis': matches,
                    'filename': row['filename_hr']
                }

# Task 3

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nTime taken to execute: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def run_stream():
    gen = mi_patient_streamer('ptbxl_database.csv', outputDictionary)

    count = 0
    for patient in gen:
        print(patient)
        count += 1
        if count == 5:
            break
        
run_stream()