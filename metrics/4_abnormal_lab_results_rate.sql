/*
    Abnormal Lab Results
    (Number of lab results with `abnormal_flag = true`) / (total number of lab results)
*/
SELECT count(case when abnormal_flag = 'True' then 1 end) * 1.0 / count(*) AS abnormal_rate
FROM lab_results
;