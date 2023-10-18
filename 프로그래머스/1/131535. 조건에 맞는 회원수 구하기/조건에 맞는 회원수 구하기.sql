SELECT count(user_id) as users
FROM user_info
WHERE YEAR(joined) = 2021 AND age BETWEEN 20 AND 29