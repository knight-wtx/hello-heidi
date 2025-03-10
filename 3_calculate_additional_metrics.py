#!/usr/bin/python

import sqlite3

def main():

    with open('metrics/5_orphan_records_rate.sql', 'r') as file:
        sql_calcualte_orphan_records_rate = file.read()

    with open('metrics/6_registration_rate.sql', 'r') as file:
        sql_calcualte_registration_rate = file.read()

    with sqlite3.connect("hello-heidi.sqlite") as db:
                
        print('[5. Calculating Orphan Records Rate]:\n')
        print(f'{sql_calcualte_orphan_records_rate}\n')
        orphan_records_rate =  db.execute(sql_calcualte_orphan_records_rate).fetchall()
        print('Orphan Records Rate:')
        for r in orphan_records_rate:
            print(f'  {r[0]} - {r[1]} in {r[2]} ({round(100*r[1]/r[2],1)}%)')

        print('\n[6. Calculating Registration Rate]:\n')
        print(f'{sql_calcualte_registration_rate}\n')
        registration_rate =  db.execute(sql_calcualte_registration_rate).fetchall()
        print(f'Registration Rate: {registration_rate[0][0]} in {registration_rate[0][1]}'
            , f'({round(100*registration_rate[0][0]/registration_rate[0][1],1)}%)')

if __name__ == '__main__':
    main()