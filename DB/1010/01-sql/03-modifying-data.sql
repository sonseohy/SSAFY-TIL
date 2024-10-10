-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO articles(title, content, createdAt)
VALUES ('hello', 'world', '2024-10-10');

SELECT * FROM articles;

INSERT INTO
  articles(title, content, createdAt)
VALUES
  ('title1', 'content1', '2020-10-10'),
  ('title2', 'content2', '2020-11-10'),
  ('title3', 'content3', '2020-12-10');

INSERT INTO articles
VALUES (10, 'hello', 'world', '2024-10-10');

INSERT INTO
  articles(title, content, createdAt)
VALUES
  ('title11', 'content11', DATE());

-- 2. Update data in table
UPDATE articles
SET
  title = 'title0'
WHERE
  id = 1;

UPDATE articles
SET
  content = 'world'
WHERE
  title = 'title1'
  AND content = 'content1';

UPDATE articles
SET
  content = 'world1',
  title = 'hello'
WHERE
  title = 'title1'
  AND content = 'world';

UPDATE articles
SET
  content = 'world1',
  title = 'hello';

SELECT * FROM articles;

-- 3. Delete data from table
SELECT * FROM articles;

DELETE FROM articles
WHERE id = 1;

SELECT * FROM articles;

DELETE FROM articles
WHERE createdAt < '2021-10-10';

-- 가장 오래된 두 개의 데이터 지우기
DELETE FROM articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);

-- 2024년도에 쓴 글 다 지우기
DELETE FROM articles
WHERE id IN (
  SELECT id
  FROM articles
  WHERE createdAt LIKE '2024%'
);
