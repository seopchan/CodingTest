-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(tlno, "NONE") as TLNO
FROM patient
WHERE age <= 12 AND GEND_CD = "W"
ORDER BY age DESC, pt_name ASC;