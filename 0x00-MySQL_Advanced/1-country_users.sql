-- creates a table for the user
-- columun country is added to the table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    country VARCHAR(255) NOT NULL DEFAULT 'US'
);
