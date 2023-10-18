SELECT f.flavor
FROM first_half as f
JOIN icecream_info as i
ON f.flavor = i.flavor
WHERE ingredient_type = "fruit_based" AND total_order > 3000
ORDER BY total_order DESC