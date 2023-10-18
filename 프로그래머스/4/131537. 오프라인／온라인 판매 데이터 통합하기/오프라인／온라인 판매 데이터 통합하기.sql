SELECT date_format(u.sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
FROM (
    SELECT sales_date, product_id, user_id, sales_amount
    FROM online_sale
    UNION ALL
    SELECT sales_date, product_id, NULL user_id, sales_amount
    FROM offline_sale
) as u
WHERE YEAR(u.sales_date) = 2022 AND MONTH(u.sales_date) = 3
ORDER BY sales_date, product_id, user_id ASC