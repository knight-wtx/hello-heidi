#!/usr/bin/python

import sqlite3

def main():

    with open('metrics/1_average_legth_of_stay.sql', 'r') as file:
        sql_calcualte_average_legth_of_stay = file.read()
    
    with open('metrics/2_top_3_diagnoses.sql', 'r') as file:
        sql_calcualte_top_3_diagnoses = file.read()
    
    with open('metrics/3_appointments_completion_rate.sql', 'r') as file:
        sql_calcualte_appointments_completion_rate = file.read()
    
    with open('metrics/4_abnormal_lab_results_rate.sql', 'r') as file:
        sql_calcualte_abnormal_lab_results_rate = file.read()

    with sqlite3.connect("staging.sqlite") as db:
        
        print(sql_calcualte_average_legth_of_stay)
        a =  db.execute(sql_calcualte_average_legth_of_stay).fetchall()
        print(a)

        print(sql_calcualte_top_3_diagnoses)
        a =  db.execute(sql_calcualte_top_3_diagnoses).fetchall()
        print(a)
        
        print(sql_calcualte_appointments_completion_rate)
        a =  db.execute(sql_calcualte_appointments_completion_rate).fetchall()
        print(a)
        
        print(sql_calcualte_abnormal_lab_results_rate)
        a =  db.execute(sql_calcualte_abnormal_lab_results_rate).fetchall()
        print(a)

if __name__ == '__main__':
    main()