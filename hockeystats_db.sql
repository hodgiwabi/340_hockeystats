--MySQL 340_hockeystats hockeystats_db.sql
--Tobias Hodges & Greg Sanchez

DROP TABLE IF EXISTS teams;

CREATE TABLE `teams` (
  `teamID` int(11) AUTO_INCREMENT NOT NULL,
  `teamName` varchar(31) NOT NULL,
  PRIMARY KEY (`teamID`),
  UNIQUE KEY `teamName` (`teamName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS games;

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

INSERT INTO `teams` VALUES (1, 'Wolves'), (2, 'Badgers');

INSERT INTO `games` VALUES (1, 1, 2, '2020-02-10', '21:30');
