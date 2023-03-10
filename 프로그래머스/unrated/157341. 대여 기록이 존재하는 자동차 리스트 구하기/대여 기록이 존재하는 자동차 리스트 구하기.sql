-- 코드를 입력하세요
SELECT DISTINCT CH.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
LEFT JOIN CAR_RENTAL_COMPANY_CAR CC
ON CH.CAR_ID = CC.CAR_ID
WHERE CC.CAR_TYPE = '세단' AND MONTH(CH.START_DATE) = 10
ORDER BY 1 DESC

#다른 풀이
SELECT DISTINCT A.CAR_ID
FROM (SELECT *
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE MONTH(START_DATE) = 10) A
LEFT JOIN CAR_RENTAL_COMPANY_CAR C
ON A.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE = '세단'
ORDER BY 1 DESC
