-- creates a table user in the database

CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY(id)
);
