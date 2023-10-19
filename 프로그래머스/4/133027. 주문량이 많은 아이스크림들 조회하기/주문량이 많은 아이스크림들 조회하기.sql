SELECT flavor
FROM (
    SELECT flavor, sum(total_order) total_order
    FROM (
        SELECT *
        FROM JULY
        UNION
        SELECT *
        FROM first_half
    ) as s
    GROUP BY flavor
    ORDER BY total_order DESC
) as ss
LIMIT 3