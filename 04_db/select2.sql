-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age=20;
-- SELECT * FROM users WHERE age>=20;

-- SELECT first_name, last_name, age FROM users WHERE age>=30;

-- -- users에서 age 30 이상, 성이 '김'인 사람의 성과 나이를 불러오기
-- SELECT last_name, age FROM users 
-- WHERE age >= 30 AND last_name='김' 
-- LIMIT 10; -- 그 중 10개



-- COUNT
-- SELECT COUNT(id) FROM users;



-- AVG, SUM, MIN, MAX (INT, FLOAT 처럼 숫자 컬럼만 가능, ()안에는 컬럼명)
-- 30살 이상인 사람들의 평균 나이
-- SELECT AVG(age) FROM users WHERE age >= 30;

-- users에서 잔액이 가장 높은 사람의 이름과 잔액
-- SELECT first_name, MAX(balance) FROM users;

-- users에서 30살 이상 사람들의 잔액 평균
-- SELECT AVG(balance) FROM users WHERE age >= 30;



-- wild cards
-- SELECT * FROM users WHERE age LIKE '2_';

-- 지역번호가 02인 사람만 가져오기
-- SELECT first_name, phone FROM users WHERE phone LIKE '02-%';

-- 이름이 '준'으로 끝나는 사람만
-- SELECT first_name FROM users WHERE first_name LIKE '%준' LIMIT 10;

-- 중간번호가 5114인 사람만
-- SELECT first_name, phone FROM users WHERE phone LIKE '%-5114-%';



-- ORDER
-- SELECT * FROM users ORDER BY age ASC;
-- SELECT * FROM users ORDER BY age DESC LIMIT 10;

-- SELECT age, balance FROM users ORDER BY age, balance LIMIT 10;

-- SELECT age, last_name FROM users ORDER BY age, last_name LIMIT 10; -- 먼저 나오는 애를 우선으로 정렬
-- SELECT age, last_name FROM users ORDER BY last_name, age LIMIT 10;

SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;