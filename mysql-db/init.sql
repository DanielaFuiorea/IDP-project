CREATE DATABASE IF NOT EXISTS wowzies;
USE wowzies;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    discount VARCHAR(50)
);
