--MySQL 340_hockeystats hockeystats_manip.sql
--Tobias Hodges & Greg Sanchez

-- CREATE Functionality
INSERT INTO games (home_id, away_id, game_date, game_time) VALUES
(:hometeam_input, :awayteam_input, :gamedate_input, :gametime_input);

INSERT INTO teams (team_name) VALUES
(:teamname_input);

INSERT INTO players (fname, lname, number, team_id) VALUES
(:fname_input, :lname_input, :number_input, :teamid_input);

INSERT INTO penalties (type) VALUES
(:type_input);

INSERT INTO infractions (player_id, penalty_id) VALUES
(:playerid_input, :penaltyid_input);

-- READ Functionality

SELECT team_id, team_name FROM teams;

SELECT game_id, home_id, away_id, game_date, game_time FROM games;

SELECT player_id, fname, lname, number FROM players;

SELECT penalty_id, type FROM penalties;

SELECT infraction_id, player_id, penalty_id FROM infractions;

-- UPDATE Functionality

UPDATE games SET home_id=:homeid_input, away_id=:awayid_input WHERE game_id=:gameid_input;

UPDATE teams SET team_name=:teamname_input WHERE team_id=:teamid_input;

UPDATE players SET team_id=:teamid_input WHERE player_id=:playerid_input;

UPDATE penalties SET type=:type_input WHERE penalty_id=:penaltyid_input;

UPDATE infractions SET penalty_id=:penaltyid_input WHERE infraction_id=:infractionid_input;

-- DELETE Functionality

DELETE FROM games WHERE game_id=:gameid_input;

DELETE FROM teams WHERE team_id=:teamid_input;

DELETE FROM players WHERE player_id=:playerid_input;

DELETE FROM penalties WHERE penalty_id=:penaltyid_input;

DELETE FROM infractions WHERE infraction_id=:infractionid_input;
