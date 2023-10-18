-- 코드를 입력하세요
-- 총주문량 내림차순, 출하 번호 오름차순
SELECT flavor
FROM first_half
ORDER BY total_order DESC, shipment_id ASC;