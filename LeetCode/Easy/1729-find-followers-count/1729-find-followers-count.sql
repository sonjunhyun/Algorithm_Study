# Write your MySQL query statement below
SELECT DISTINCT(USER_ID), COUNT(*) FOLLOWERS_COUNT
FROM FOLLOWERS
GROUP BY 1
ORDER BY 1