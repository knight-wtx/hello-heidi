/*
    Average Length of Stay
    For inpatient encounters (where `encounter_type = 'inpatient'`) that have a non-null `discharge_date`.  
*/
SELECT avg(julianday(discharge_date) - julianday(admission_date)) AS average_legth_of_stay
FROM encounters
WHERE encounter_type = 'inpatient' AND discharge_date IS NOT NULL
;