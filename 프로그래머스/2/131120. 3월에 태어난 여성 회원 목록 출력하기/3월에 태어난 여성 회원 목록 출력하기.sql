SELECT member_id, member_name, gender, date_format(date_of_birth, "%Y-%m-%d") as date_of_birth
FROM member_profile
WHERE gender = "W" AND MONTH(date_of_birth) = 3 AND NOT ISNULL(tlno)
ORDER BY member_id