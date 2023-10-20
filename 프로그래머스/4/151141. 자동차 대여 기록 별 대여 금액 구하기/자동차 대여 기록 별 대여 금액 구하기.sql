SELECT history_id,
CASE
    WHEN days BETWEEN 7 AND 29 
    THEN ROUND(A.fee * (100 - (SELECT discount_rate FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '7일 이상' AND car_type = "트럭")) / 100)
    WHEN days BETWEEN 30 AND 89 
    THEN ROUND(A.fee * (100 - (SELECT discount_rate FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '30일 이상' AND car_type = "트럭")) / 100)
    WHEN days >= 90 
    THEN ROUND(A.fee * (100 - (SELECT discount_rate FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '90일 이상' AND car_type = "트럭")) / 100)
    ELSE A.fee
END as FEE
FROM (
    SELECT history_id,
    (datediff(end_date, start_date) + 1) days,
    daily_fee * (datediff(end_date, start_date) + 1) as FEE
    FROM CAR_RENTAL_COMPANY_CAR
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
    USING (car_id)
    WHERE car_type = "트럭"
) as A
ORDER BY fee DESC, history_id DESC