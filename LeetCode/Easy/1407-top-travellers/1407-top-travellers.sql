# Write your MySQL query statement below
SELECT U.NAME, IFNULL(SUM(R.DISTANCE), 0) TRAVELLED_DISTANCE
FROM USERS U
LEFT JOIN RIDES R
ON U.ID = R.USER_ID
GROUP BY 1, R.USER_ID
ORDER BY 2 DESC, 1 ASC