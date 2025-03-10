SELECT
    COUNT(CASE WHEN status = 'completed' THEN 1 END) AS completed_appointments
    , COUNT(*) AS all_appointments
FROM
    appointments
;