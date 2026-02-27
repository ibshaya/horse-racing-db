DROP VIEW IF EXISTS horses_by_owner;
DROP VIEW IF EXISTS winning_trainers;
DROP VIEW IF EXISTS trainer_total_winnings;
DROP VIEW IF EXISTS track_stats;

USE racing;


CREATE VIEW horses_by_owner AS
SELECT 
    o.lname AS OwnerLastName,
    h.horseName AS Horse,
    h.age AS Age,
    t.fname AS TrainerFirst,
    t.lname AS TrainerLast
FROM Owner o
JOIN Owns ow ON o.ownerId = ow.ownerId
JOIN Horse h ON ow.horseId = h.horseId
JOIN Trainer t ON t.stableId = h.stableId;





CREATE VIEW winning_trainers AS
SELECT 
    t.fname AS TrainerFirst,
    t.lname AS TrainerLast,
    h.horseName AS Horse,
    r.raceName AS Race,
    r.trackName AS Track
FROM Trainer t
JOIN Horse h ON t.stableId = h.stableId
JOIN RaceResults rr ON h.horseId = rr.horseId
JOIN Race r ON rr.raceId = r.raceId
WHERE rr.results = 'first';




CREATE VIEW trainer_total_winnings AS
SELECT 
    t.fname AS TrainerFirst,
    t.lname AS TrainerLast,
    SUM(rr.prize) AS TotalPrize
FROM Trainer t
JOIN Horse h ON t.stableId = h.stableId
JOIN RaceResults rr ON h.horseId = rr.horseId
GROUP BY t.trainerId
ORDER BY TotalPrize DESC;



CREATE VIEW track_stats AS
SELECT 
    tr.trackName,
    COUNT(DISTINCT r.raceId) AS RaceCount,
    COUNT(DISTINCT rr.horseId) AS HorseCount
FROM Track tr
JOIN Race r ON tr.trackName = r.trackName
JOIN RaceResults rr ON r.raceId = rr.raceId
GROUP BY tr.trackName;

