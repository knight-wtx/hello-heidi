#!/usr/bin/python

import csv
import json
import re
import sqlite3

def parse_csv_to_list_of_dict(input_file_path):
    with open(input_file_path) as f:
        output = list(csv.DictReader(f))
        return output

def parse_json_to_list_of_dict(input_file_path):
    with open(input_file_path) as f:
        output = json.load(f)
        return output

def parse_event_details_to_dict(input_string):
    output = {}
    match_pattern = r'(.*)="(.*)"'
    for key_value_pair in input_string.split(" "):
        match_result = re.findall(match_pattern, key_value_pair)[0]
        output[match_result[0]] = match_result[1]
    return output

def parse_log_to_list_of_dict(input_file_path):
    with open(input_file_path) as f:
        output = []
        match_pattern = r'\[(.*)\] ([^=]*)=([^=]*) (.*)'
        for line in f.read().splitlines():
            match_result = re.findall(match_pattern, line)[0]
            event_struct = {
                "timestamp": match_result[0]
                , match_result[1]: match_result[2]
                , "details": parse_event_details_to_dict(match_result[3])
            }
            output.append(event_struct)
        return output

def generate_sql_from_list_of_dict(target_table_name, list_of_dict):
    sql_drop = f'DROP TABLE IF EXISTS {target_table_name};\n'
    sql_ctas = f'CREATE TABLE {target_table_name} AS\n'
    sql_select_all = []
    for d in list_of_dict:
        sql_select_one = []
        for key, value in d.items():
            value = json.dumps(value) if isinstance(value, dict) else value
            sql_select_one.append(f"'{value}' AS {key}")
        sql_select = 'SELECT ' + ', '.join(sql_select_one)
        sql_select_all.append(sql_select)
    output = sql_drop + sql_ctas + ' UNION ALL\n'.join(sql_select_all) + ';'
    return output

def main():

    with open('data/sql/patients.sql', 'r') as file:
        sql_load_patients_data = file.read()

    with open('data/sql/encounters.sql', 'r') as file:
        sql_load_encounters_data = file.read()

    with open('data/sql/diagnoses.sql', 'r') as file:
        sql_load_diagnoses_data = file.read()

    appointments_data = parse_csv_to_list_of_dict('data/files/appointments.csv')
    sql_load_appointments_data = generate_sql_from_list_of_dict('appointments', appointments_data)

    lab_results_data = parse_json_to_list_of_dict('data/files/lab_results.json')
    sql_load_lab_results_data = generate_sql_from_list_of_dict('lab_results', lab_results_data)

    staff_activity_data = parse_log_to_list_of_dict('data/files/staff_activity.log')
    sql_load_staff_activity_data = generate_sql_from_list_of_dict('staff_activities', staff_activity_data)

    with sqlite3.connect("hello-heidi.sqlite") as db:

        print('Loading patients data:\n')
        print(f'{sql_load_patients_data}\n')
        db.executescript(sql_load_patients_data)

        print('Loading encounters data:\n')
        print(f'{sql_load_encounters_data}\n')
        db.executescript(sql_load_encounters_data)

        print('Loading diagnoses data:\n')
        print(f'{sql_load_diagnoses_data}\n')
        db.executescript(sql_load_diagnoses_data)

        print('Loading appointments data:\n')
        print(f'{sql_load_appointments_data}\n')
        db.executescript(sql_load_appointments_data)

        print('Loading staff activity data:\n')
        print(f'{sql_load_staff_activity_data}\n')
        db.executescript(sql_load_staff_activity_data)

        print('Loading lab results data:\n')
        print(f'{sql_load_lab_results_data}\n')
        db.executescript(sql_load_lab_results_data)
        
if __name__ == '__main__':
    main()