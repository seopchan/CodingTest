SELECT user_id, nickname, sum(price) as total_sales
FROM used_goods_board
JOIN used_goods_user
ON writer_id = user_id
WHERE status = "DONE"
GROUP BY writer_id
HAVING total_sales >= 700000
ORDER BY total_sales    