/*    
    While the subquery is sufficient to find diagnoses by frequency, it does not handle ties 
    gracefully. Hence an additional step is taken to group the tying codes (as string or array) 
    by frequency. The query would return all the diagnoses codes that belong to each one of the
    top 3 frequency counts.
*/
SELECT
    JSON_GROUP_ARRAY(code) AS code_array
    , GROUP_CONCAT(code, ', ') AS code_string
    , freq
FROM (
    SELECT code, COUNT(*) AS freq
    FROM diagnoses
    GROUP BY 1
)
GROUP BY freq
ORDER BY 3 DESC
LIMIT 3
;