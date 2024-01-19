-- stored procedure add bonus
DELIMITER $$
CREATE PROCEDURE add_bonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;