-- Script that prepares a MySQL server for the project

--Creates user
CREATE USER IF NOT EXISTS 'hbnb_dev' @ 'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
--Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db
USE hbnb_dev_db

-- Grant Privileges to user hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @ 'localhost'
FLUSH PRIVILEGES

GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @ 'localhost'
FLUSH PRIVILEGES
