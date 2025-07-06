CREATE DATABASE IF NOT EXISTS ai_dungeon;
USE ai_dungeon;

CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(30),
    health INT,
    inventory TEXT
);
