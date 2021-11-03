-- Create second table in database
CREATE table IF not exists second_table (
    id int,
    name varchar(256),
    score int
    );

INSERT into second_table (id, name, score)
VALUES
(1, "John", 10), 
(2, "Alex", 3),
(3, "Bob", 14), 
(4, "George", 8);