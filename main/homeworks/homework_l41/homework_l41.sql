/* Создание базы данных */
CREATE DATABASE local_network;

/* Подключаемся к созданной БД */
USE local_network;

/* Создаём таблицу local_network */
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(30) NOT NULL,
    ip_address VARCHAR(15) NOT NULL,
	comp_name VARCHAR(40) NOT NULL,
	domain VARCHAR(40) NOT NULL);

/* Наполнение таблицы данными */
INSERT INTO users (user_name, ip_address, comp_name, domain) VALUES
("Andrew", "192.168.311.23", "sysadm", "office_1"),
("Vasilii", "192.168.311.25", "energo", "office_1"),
("Marina", "192.168.312.30", "glav_buh", "buh_office"),
("Darina", "192.168.312.31", "buh_1", "buh_office"),
("Lidia", "192.168.312.32", "economist", "buh_office"),
("Lilia", "192.168.312.33", "auditor", "buh_office"),
("Alexey", "192.168.311.27", "law", "office_1"),
("Nikolay", "192.168.311.28", "prorab", "office_1");

/* Работа с таблицей */

-- Сменим название столбца domain на offices
alter table users change column domain offices varchar(40) not null;

-- Общая выборка по таблице users
select * from users;

-- Выборка по полю user_name
select user_name from users;
