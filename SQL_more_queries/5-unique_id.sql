-- Task 5: Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);