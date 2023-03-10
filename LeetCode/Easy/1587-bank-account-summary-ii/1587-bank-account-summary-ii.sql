# Write your MySQL query statement below
SELECT NAME, SUM(AMOUNT) BALANCE
FROM USERS U, TRANSACTIONS T
WHERE U.ACCOUNT = T.ACCOUNT
GROUP BY 1
HAVING SUM(AMOUNT) > 10000