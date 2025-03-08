SELECT COUNT(CASE WHEN abnormal_flag = 'True' THEN 1 END) * 1.0 / COUNT(*) AS abnormal_rate
FROM lab_results;