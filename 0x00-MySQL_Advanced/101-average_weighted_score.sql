-- CREATE ComputeAverageWeightedScoreForUser for all
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT DEFAULT 0; 
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections, projects
        WHERE corrections.project_id = projects.id
        AND corrections.user_id = users.id
                        )
    
END $$
DELIMITER ;