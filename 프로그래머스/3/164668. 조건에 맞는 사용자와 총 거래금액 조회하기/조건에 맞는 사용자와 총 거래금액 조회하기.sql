SELECT user_id, nickname, total_sales
FROM (
    SELECT sum(price) as total_sales, writer_id, status
    FROM used_goods_board
    WHERE status = "DONE"
    GROUP BY writer_id
    HAVING total_sales >= 700000
    ORDER BY total_sales    
) as p
JOIN used_goods_user as u
ON p.writer_id = u.user_id
