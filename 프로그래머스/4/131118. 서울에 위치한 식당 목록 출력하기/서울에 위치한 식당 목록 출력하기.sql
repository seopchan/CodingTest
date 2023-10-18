SELECT i.rest_id, rest_name, food_type, favorites, address, round(avg(review_score), 2) as score
FROM rest_info as i
JOIN rest_review as r
ON i.rest_id = r.rest_id
WHERE address LIKE "서울%"
GROUP BY rest_name
ORDER BY score DESC, favorites DESC