-- Create table users 
-- Create table users

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
