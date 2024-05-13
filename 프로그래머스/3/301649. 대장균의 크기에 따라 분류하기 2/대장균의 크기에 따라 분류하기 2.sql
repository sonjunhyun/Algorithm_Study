-- 코드를 작성해주세요
WITH A AS (
    SELECT ID,
           PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS PCT
    FROM ECOLI_DATA
)
    
SELECT ID, CASE
                WHEN PCT <= 0.25 THEN 'CRITICAL'
                WHEN PCT <= 0.5 THEN 'HIGH'
                WHEN PCT <= 0.75 THEN 'MEDIUM'
                ELSE 'LOW'
           END AS COLONY_NAME
FROM A
ORDER BY 1