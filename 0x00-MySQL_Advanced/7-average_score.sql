-- average score stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT DEFAULT 0;
    
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user_id;
    
    UPDATE users SET average_score = average_score WHERE id = user_id;
END $$
DELIMITER ;
