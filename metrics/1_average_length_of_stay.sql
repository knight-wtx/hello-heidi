SELECT
    AVG(
        JULIANDAY(discharge_date)
        - JULIANDAY(admission_date)
    ) AS average_length_of_stay
FROM
    encounters
WHERE
    encounter_type = 'inpatient'
    AND discharge_date IS NOT NULL
;