-- MySQL 340_hockeystats hockeystats_db.sql
-- Tobias Hodges & Greg Sanchez

DROP TABLE IF EXISTS infractions;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS penalties;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE `teams` (
  `team_id` int(11) AUTO_INCREMENT NOT NULL,
  `team_name` varchar(31) NOT NULL,
  PRIMARY KEY (`team_id`),
  UNIQUE KEY `team_name` (`team_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `games` (
  `game_id` int(11) AUTO_INCREMENT NOT NULL,
  `home_id` int(11),
  `away_id` int(11),
  `game_date` DATE NOT NULL,
  `game_time` TIME NOT NULL,
  PRIMARY KEY (`game_id`),
  UNIQUE KEY `game_time_date` (`game_time`, `game_date`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`home_id`) REFERENCES `teams` (`team_id`) ON DELETE CASCADE,
  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`away_id`) REFERENCES `teams` (`team_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `players` (
  `player_id` int(11) AUTO_INCREMENT NOT NULL,
  `fname` varchar(31) NOT NULL,
  `lname` varchar(31) NOT NULL,
  `number` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `total_points` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`player_id`),
  UNIQUE KEY `playerName` (`fname`, `lname`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `penalties` (
  `penalty_id` int(11) AUTO_INCREMENT NOT NULL,
  `type` varchar(31) NOT NULL,
  PRIMARY KEY (`penalty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `infractions` (
  `infraction_id` int(11) AUTO_INCREMENT NOT NULL,
  `player_id` int(11) NOT NULL,
  `penalty_id` int(11) NOT NULL,
  PRIMARY KEY (`infraction_id`),
  CONSTRAINT `infractions_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`) ON DELETE CASCADE,
  CONSTRAINT `infractions_ibfk_2` FOREIGN KEY (`penalty_id`) REFERENCES `penalties` (`penalty_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `teams` VALUES (1, 'Wolves'),(2, 'Badgers');

INSERT INTO `games` VALUES (1, 1, 2, '2020-02-10', '21:30');

INSERT INTO `players` VALUES (1, 'Jim', 'Halpert', 11, 1, 0),(2, 'Pam', 'Anderson', 25, 2, 0);

INSERT INTO `penalties` VALUES (1, 'Hooking');

INSERT INTO `infractions` VALUES (1, 1, 1);
