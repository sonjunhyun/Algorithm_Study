-- 코드를 작성해주세요
SELECT COUNT(*) AS `COUNT`
FROM ECOLI_DATA
WHERE (GENOTYPE & 2 IS FALSE) && ((GENOTYPE & 1) || (GENOTYPE & 4)) IS TRUE