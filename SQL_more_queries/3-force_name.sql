-- Task 4: Write a script that creates a table called first_table in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);