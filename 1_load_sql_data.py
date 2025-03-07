#!/usr/bin/python

import sqlite3

def main():
  with sqlite3.connect("hello-heidi.sqlite") as db:

    with open('source/sql/patients.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    with open('source/sql/encounters.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    with open('source/sql/diagnoses.sql', 'r') as file:
      query = file.read().replace('\n', '')
      db.executescript(query)

    # data1 = db.execute('SELECT * FROM patients').fetchall()
    # data2 = db.execute('SELECT * FROM encounters').fetchall()
    # data3 = db.execute('SELECT * FROM diagnoses').fetchall()
    # print(data1)
    # print(data2)
    # print(data3)

if __name__ == '__main__':
  main()