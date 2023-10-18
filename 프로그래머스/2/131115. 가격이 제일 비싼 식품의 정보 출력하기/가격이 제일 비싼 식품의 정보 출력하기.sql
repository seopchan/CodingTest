SET @MAX := (
    SELECT MAX(price)
    FROM food_product
);
SELECT *
FROM food_product
WHERE price = @MAX