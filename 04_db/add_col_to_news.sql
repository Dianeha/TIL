ALTER TABLE news ADD COLUMN created_at DATETIME 
NOT NULL DEFAULT 1;
-- 새로운 컬럼(created_at)을 NOT NULL 조건으로 생성할 때 기존 데이터에 
-- 해당 컬럼의 값이 없기 때문에 에러가 난다 >> DEFAULT 값을 지정해 비어있는 곳에 다 1을 넣어준다.
