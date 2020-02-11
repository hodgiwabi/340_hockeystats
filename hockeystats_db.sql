--MySQL 340_hockeystats hockeystats_db.sql
--Tobias Hodges & Greg Sanchez

DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS penalties;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE `teams` (
  `teamID` int(11) AUTO_INCREMENT NOT NULL,
  `teamName` varchar(31) NOT NULL,
  PRIMARY KEY (`teamID`),
  UNIQUE KEY `teamName` (`teamName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `games` (
  `gameID` int(11) AUTO_INCREMENT NOT NULL,
  `homeTeamID` int(11),
  `awayTeamID` int(11),
  `gameDate` DATE NOT NULL,
  `gameTime` TIME NOT NULL,
  PRIMARY KEY (`gameID`),
  UNIQUE KEY `gameTimeDate` (`gameTime`, `gameDate`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`homeTeamID`) REFERENCES `teams` (`teamID`),
  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`awayTeamID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `players` (
  `playerID` int(11) AUTO_INCREMENT NOT NULL,
  `playerFName` varchar(31) NOT NULL,
  `playerLName` varchar(31) NOT NULL,
  `playerNumber` int(11) NOT NULL,
  `playerTeamID` int(11) NOT NULL,
  PRIMARY KEY (`playerID`),
  UNIQUE KEY `playerName` (`playerFName`, `playerLName`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`playerTeamID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `penalties` (
  `penaltyID` int(11) AUTO_INCREMENT NOT NULL,
  `penaltyType` varchar(31) NOT NULL,
  `penaltyTime` int(11) NOT NULL,
  PRIMARY KEY (`penaltyID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `teams` VALUES (1, 'Wolves'), (2, 'Badgers');

INSERT INTO `games` VALUES (1, 1, 2, '2020-02-10', '21:30');

INSERT INTO `players` VALUES (1, 'Jim', 'Halpert', 11, 1);

INSERT INTO `penalties` VALUES (1, 'Hooking', 2);
