#!/usr/bin/python

import csv
import json
import re
import sqlite3

def parse_csv(input_file_path):
  with open(input_file_path) as f:
    output = list(csv.DictReader(f))
    return output

def parse_json(input_file_path):
  with open(input_file_path) as f:
    output = json.load(f)
    return output

def parse_event(input_string):
  output = {}
  match_pattern = r'(.*)="(.*)"'
  for key_value_pair in input_string.split(" "):
    match_result = re.findall(match_pattern, key_value_pair)[0]
    output[match_result[0]] = match_result[1]
  return output
  
def parse_log(input_file_path):
  with open(input_file_path) as f:
    output = []
    match_pattern = r'\[(.*)\] ([^=]*)=([^=]*) (.*)'
    for line in f.read().splitlines():
      match_result = re.findall(match_pattern, line)[0]
      event_struct = {
        "timestamp": match_result[0]
        , match_result[1]: match_result[2]
        , "details": parse_event(match_result[3])
      }
      output.append(event_struct)
    return output

def load_sqlite(db_name, table_name, data):
  
  db = sqlite3.connect("heidi.sqlite")
  c = db.cursor()

def main():
  # appointments_data = parse_csv('source/appointments.csv')
  # print(appointments_data)

  # lab_results_data = parse_json('source/lab_results.json')
  # print(lab_results_data)

  # staff_activity_data = parse_log('source/staff_activity.log')
  # print(staff_activity_data)
  

  with sqlite3.connect(":memory:") as db:

    with open('source/sql/patients.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    with open('source/sql/encounters.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    with open('source/sql/diagnoses.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    data1 = db.execute('SELECT * FROM patients').fetchall()
    data2 = db.execute('SELECT * FROM encounters').fetchall()
    data3 = db.execute('SELECT * FROM diagnoses').fetchall()
    print(data1)
    print(data2)
    print(data3)

if __name__ == '__main__':
  main()