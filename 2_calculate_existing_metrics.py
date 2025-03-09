#!/usr/bin/python

import sqlite3

def main():

    with open('metrics/1_average_length_of_stay.sql', 'r') as file:
        sql_calcualte_average_length_of_stay = file.read()
    
    with open('metrics/2_top_3_diagnoses.sql', 'r') as file:
        sql_calcualte_top_3_diagnoses = file.read()
    
    with open('metrics/3_appointments_completion_rate.sql', 'r') as file:
        sql_calcualte_appointments_completion_rate = file.read()
    
    with open('metrics/4_abnormal_lab_results_pct.sql', 'r') as file:
        sql_calcualte_abnormal_lab_results_pct = file.read()

    with sqlite3.connect("hello-heidi.sqlite") as db:
        
        print('[1. Calculating Average Length of Stay]:\n')
        print(f'{sql_calcualte_average_length_of_stay}\n')
        average_length_of_stay =  db.execute(sql_calcualte_average_length_of_stay).fetchall()
        print(f'Average Length of Stay: {round(average_length_of_stay[0][0], 2)} days.\n')

        print('[2. Calculating Top 3 Diagnoses]:\n')
        print(f'{sql_calcualte_top_3_diagnoses}\n')
        top_3_diagnoses =  db.execute(sql_calcualte_top_3_diagnoses).fetchall()
        print('Top 3 Diagnoses:')
        for r in top_3_diagnoses:
            print(f'  Frequency = {r[2]} : {r[1]}')
        
        print('\n[3. Calculating Appointments Completion Rate]:\n')
        print(f'{sql_calcualte_appointments_completion_rate}\n')
        appointments_completion_rate =  db.execute(sql_calcualte_appointments_completion_rate).fetchall()
        print(f'Appointments Completion Rate: {appointments_completion_rate[0][0]} in {appointments_completion_rate[0][1]}'
            , f'({round(appointments_completion_rate[0][0]/appointments_completion_rate[0][1],1)}).\n')

        
        print('[4. Calculating Abnormal Lab Results Percentage]:\n')
        print(f'{sql_calcualte_abnormal_lab_results_pct}\n')
        abnormal_lab_results_rate =  db.execute(sql_calcualte_abnormal_lab_results_pct).fetchall()
        print(f'Abnormal Lab Results Percentage: {abnormal_lab_results_rate[0][0]} in {abnormal_lab_results_rate[0][1]}'
            , f'({round(100*abnormal_lab_results_rate[0][0]/abnormal_lab_results_rate[0][1],1)}%).\n')

if __name__ == '__main__':
    main()