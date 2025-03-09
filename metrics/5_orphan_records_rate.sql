/*
    An orphan record is a row in the child table where the value of a foreign key column in the 
    child table does not exist in the referencing column in the parent table. Orphan records may 
    occur for a number of reasons, such as:
        - primary table's data updated or deleted
        - data inconsistency across multiple systems 
        - child table's data arriving earlier than parent table's data
        - etc.
    Orphan records rate is a useful data quality metrics. It can be used in:
        - evalutating data's suitability for specific use cases
        - investigating system flaws and developing enhancement
        - monitoring unexpected incidents or issues with business process
        - etc.
*/
SELECT
    'appointments.patient_id' AS table_column
    , COUNT(CASE WHEN p.patient_id IS NULL THEN 1 END) AS orphan_records
    , COUNT(*) AS total_records
FROM
    appointments AS a
    LEFT JOIN patients AS p
        ON a.patient_id = p.patient_id
UNION ALL
SELECT
    'lab_results.encounter_id' AS table_column
    , COUNT(CASE WHEN e.encounter_id IS NULL THEN 1 END) AS orphan_records
    , COUNT(*) AS total_records
FROM
    lab_results AS l
    LEFT JOIN encounters AS e
        ON l.encounter_id = e.encounter_id
;