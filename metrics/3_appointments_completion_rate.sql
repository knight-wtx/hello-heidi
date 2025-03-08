SELECT COUNT(CASE WHEN status = 'completed' THEN 1 END) * 1.0 / COUNT(*) AS completion_rate
FROM appointments;