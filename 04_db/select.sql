-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;
-- SELECT * FROM classmates;

-- LIMIT & OFFSET
-- SELECT * FROM classmates LIMIT 2; -- 앞에서 두개만
-- SELECT * FROM classmates LIMIT 1 OFFSET 2; -- 앞에 두 개 띄고 한개만 
-- SELECT * FROM classmates LIMIT 50 OFFSET 50;  -- 게시판, 50개씩 묶기

-- WHERE
-- SELECT * FROM classmates where name='권연주';
-- SELECT * FROM classmates where address='대구광역시' LIMIT 1; -- 주소가 '대구광역시'인 사람 중 2명

-- DISTINCT
SELECT DISTINCT age FROM classmates;
