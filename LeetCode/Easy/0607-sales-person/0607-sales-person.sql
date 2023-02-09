# Write your MySQL query statement below
SELECT S.NAME
FROM SALESPERSON S
WHERE S.SALES_ID NOT IN (SELECT O.SALES_ID
                        FROM ORDERS O
                        LEFT JOIN COMPANY C
                        ON O.COM_ID = C.COM_ID
                        WHERE C.NAME = 'RED')