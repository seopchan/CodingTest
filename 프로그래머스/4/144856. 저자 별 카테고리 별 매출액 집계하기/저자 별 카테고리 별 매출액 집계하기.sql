SELECT a.author_id, author_name, category, sum(sp) as total_sales
FROM (
    -- 책 판매 가격
    SELECT b.book_id, category, author_id, (sales * price) as sp
    FROM (
        -- 22년 1월 책 판매량
        SELECT s.book_id, sum(sales) as sales
        FROM book_sales AS s
        WHERE YEAR(sales_date) = 2022 AND MONTH(sales_date) = 1
        GROUP BY s.book_id
    ) as s
    JOIN book AS b
    ON s.book_id = b.book_id
) as sub
JOIN author a
ON sub.author_id = a.author_id
GROUP BY a.author_id, category
ORDER BY a.author_id, category DESC