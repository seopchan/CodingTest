SELECT animal_id, name
FROM animal_ins
WHERE NOT intake_condition = "Aged"
ORDER BY animal_id