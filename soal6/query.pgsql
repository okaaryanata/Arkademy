DROP DATABASE arkademy;
CREATE DATABASE arkademy;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name varchar(255)
);
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO users(name) VALUES('Robert');
INSERT INTO users(name) VALUES('Turah Marcel');

INSERT INTO skills(name,user_id) VALUES('Java',1);
INSERT INTO skills(name,user_id) VALUES('Python',1);
INSERT INTO skills(name,user_id) VALUES('Go',1);
INSERT INTO skills(name,user_id) VALUES('PHP',2);
INSERT INTO skills(name,user_id) VALUES('Ruby',2);

-- NMR 6 PART A
SELECT U.name nama_programmer, count(S.name) jumlah_skill FROM users U
JOIN skills S on U.id = S.user_id
GROUP BY U.NAME;