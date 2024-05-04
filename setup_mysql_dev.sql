-- Create a development database
CREATE DATABASE IF NOT EXISTS my_dev_database;

-- Use the development database
USE my_dev_database;

-- Create a table
CREATE TABLE IF NOT EXISTS my_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create a user for development
CREATE USER 'alvin'@'localhost' IDENTIFIED BY 'root';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON my_dev_database.* TO 'alvin'@'localhost';
