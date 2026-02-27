DROP PROCEDURE IF EXISTS add_new_race_with_results;
DROP PROCEDURE IF EXISTS delete_owner;
DROP PROCEDURE IF EXISTS move_horse;
DROP PROCEDURE IF EXISTS approve_new_trainer;

USE racing;

CREATE PROCEDURE add_new_race_with_results(
    IN p_raceId VARCHAR(15),
    IN p_raceName VARCHAR(30),
    IN p_trackName VARCHAR(30),
    IN p_raceDate DATE,
    IN p_raceTime TIME,
    IN p_horseId VARCHAR(15),
    IN p_results VARCHAR(15),
    IN p_prize FLOAT(10,2)
)
BEGIN
    INSERT INTO Race VALUES (p_raceId, p_raceName, p_trackName, p_raceDate, p_raceTime);
    INSERT INTO RaceResults VALUES (p_raceId, p_horseId, p_results, p_prize);
END;



CREATE PROCEDURE delete_owner(IN p_ownerId VARCHAR(15))
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE v_horseId VARCHAR(15);

    
    DECLARE horse_cursor CURSOR FOR
        SELECT horseId
        FROM Owns
        WHERE ownerId = p_ownerId;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN horse_cursor;

    read_loop: LOOP
        FETCH horse_cursor INTO v_horseId;
        IF done THEN
            LEAVE read_loop;
        END IF;

        
        IF (SELECT COUNT(*) FROM Owns WHERE horseId = v_horseId) = 1 THEN
            
            DELETE FROM RaceResults WHERE horseId = v_horseId;

             
            DELETE FROM Horse WHERE horseId = v_horseId;
        END IF;

        
        DELETE FROM Owns WHERE horseId = v_horseId AND ownerId = p_ownerId;
    END LOOP;

    CLOSE horse_cursor;

    DELETE FROM Owner WHERE ownerId = p_ownerId;
END;



CREATE PROCEDURE move_horse(
    IN p_horseId VARCHAR(15),
    IN p_newStableId VARCHAR(15)
)
BEGIN
    UPDATE Horse
    SET stableId = p_newStableId
    WHERE horseId = p_horseId;
END;



CREATE PROCEDURE approve_new_trainer(
    IN p_trainerId VARCHAR(15),
    IN p_lname VARCHAR(30),
    IN p_fname VARCHAR(30),
    IN p_stableId VARCHAR(15)
)
BEGIN
    INSERT INTO Trainer VALUES (p_trainerId, p_lname, p_fname, p_stableId);
END;



CREATE TABLE IF NOT EXISTS old_info AS SELECT * FROM Horse WHERE 1=0;

CREATE TRIGGER before_horse_delete
BEFORE DELETE ON Horse
FOR EACH ROW
BEGIN
    INSERT INTO old_info VALUES (
        OLD.horseId,
        OLD.horseName,
        OLD.age,
        OLD.gender,
        OLD.registration,
        OLD.stableId
    );
END;
