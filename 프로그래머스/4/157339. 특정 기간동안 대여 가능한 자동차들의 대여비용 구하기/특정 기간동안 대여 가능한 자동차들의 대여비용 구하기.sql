SELECT car_id, car_type, round((daily_fee * 30 * (100-discount_rate) / 100)) AS fee
FROM car_rental_company_car c
LEFT JOIN (
    SELECT *
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE '2022-11-01' BETWEEN start_date AND end_date 
    OR '2022-11-30' BETWEEN start_date AND end_date    
) as sub
USING (car_id)
JOIN (
    SELECT *
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE duration_type = "30일 이상"
) as sub2
USING (car_type)
WHERE c.car_type IN ("세단", "SUV") AND history_id IS NULL
HAVING fee BETWEEN 500000 AND 1999999
ORDER BY fee DESC, car_type ASC, car_id DESC