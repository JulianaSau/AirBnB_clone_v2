-- Prepares a MySQL test server for the AirBnB clone

-- Create User
CREATE USER IF NOT EXISTS 'hbnb_test' @ 'localhost' IDENTIFIED BY 'hbnb_test_pwd'
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db
USE hbnb_test_db

-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @ 'localhost'
FLUSH PRIVILEGES

GRANT SELECT ON performance_schema.* TO 'hbnb_test' @ 'localhost'
FLUSH PRIVILEGES
