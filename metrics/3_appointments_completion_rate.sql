/*
    Appointment Completion Rate
    (Number of appointments with `status = 'completed'`) / (total number of appointments)
*/
SELECT count(case when status = 'completed' then 1 end) * 1.0 / count(*) AS completion_rate
FROM appointments
;