SELECT count(a.name)
FROM (
    SELECT name
    FROM animal_ins
    GROUP BY name
) as a