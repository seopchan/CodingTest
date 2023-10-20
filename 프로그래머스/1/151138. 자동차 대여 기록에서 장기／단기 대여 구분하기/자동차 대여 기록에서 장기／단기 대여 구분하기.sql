SELECT history_id, car_id, date_format(start_date, "%Y-%m-%d") START_DATE, date_format(end_date, "%Y-%m-%d") END_DATE, IF(DATEDIFF(end_date, start_date) + 1 >= 30, "장기 대여", "단기 대여") RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE month(start_date) = 9
ORDER BY history_id DESC