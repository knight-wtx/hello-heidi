SELECT
    COUNT(CASE WHEN abnormal_flag = 'True' THEN 1 END) AS abnormal_results
    , COUNT(*) AS all_results
FROM
    lab_results
;