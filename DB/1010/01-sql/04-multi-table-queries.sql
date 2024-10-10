-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE users.name = '하석주';

-- LEFT JOIN


-- 실습2
CREATE TABLE roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  role VARCHAR(50) NOT NULL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  roleId INTEGER NOT NULL,
  Foreign Key (roleId)
    REFERENCES roles(id)
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  roles (role)
VALUES 
  ('admin'),
  ('staff'),
  ('student');

INSERT INTO 
  users (name, roleId)
VALUES 
  ('하석주', 1),
  ('송윤미', 3),
  ('유하선', 2);

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM roles;
SELECT * FROM users;
SELECT* FROM articles;

-- INNER JOIN
SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE users.name = '하석주';

SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id
INNER JOIN roles
  ON users.roleId = roles.id
WHERE role = 'student';

-- LEFT JOIN
SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;

SELECT * FROM users
LEFT JOIN articles
  ON articles.userId = users.id;

-- 게시글을 작성한 이력이 없는 사람
SELECT name FROM users
LEFT JOIN articles
  ON articles.userId = users.id
WHERE
  userId is NULL;