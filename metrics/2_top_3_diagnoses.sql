/*
    Top 3 Diagnoses
    By frequency of the code field.
*/
SELECT
    json_group_array(code) AS code
    , freq
FROM (
    SELECT code, count(*) AS freq
    FROM diagnoses
    GROUP BY 1
)
GROUP BY freq
ORDER BY 2 DESC
LIMIT 3
;
/*    
    While the subquery is sufficient to find the top diagnoses by frequency, it does not handle 
    ties gracefully. Hence an additional step is taken to group the tying codes by frequency.
    The query would return all the diagnoses that belong to each one of the top 3 frequency counts.
*/