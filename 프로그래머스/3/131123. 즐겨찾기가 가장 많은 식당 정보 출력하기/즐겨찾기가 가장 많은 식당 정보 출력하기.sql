SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
FROM (
    SELECT food_type, MAX(favorites) as max_favorites
    FROM rest_info
    GROUP BY food_type
) as sub
JOIN rest_info AS r ON sub.food_type = r.food_type AND sub.max_favorites = r.favorites
ORDER BY r.food_type DESC;