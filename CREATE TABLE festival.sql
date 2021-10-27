CREATE TABLE festival
  (
     festivalID          INT4 NOT NULL,
     festivalStartingDate DATE,
     festivalEndingDate   DATE,
     PRIMARY KEY (festivalID)
  );

CREATE TABLE ticket
  (
     ticketID        INT4 NOT NULL,
     price            FLOAT4 NOT NULL,
     place            VARCHAR(255),
     sellingPage      VARCHAR(255),
     eventID          INT4 NOT NULL,
     ticketVendorName VARCHAR(255) NOT NULL,
     PRIMARY KEY (ticketID)
  );

CREATE TABLE localization
  (
     localizationID   INT4 NOT NULL,
     localizationName VARCHAR(50) NOT NULL,
     postCode         VARCHAR(6) NOT NULL,
     adress           VARCHAR(255) NOT NULL,
     cityID           INT4 NOT NULL,
     PRIMARY KEY (localizationID)
  );

CREATE TABLE "user"
  (
     userID   INT4 NOT NULL,
     username VARCHAR(40) NOT NULL UNIQUE,
     password VARCHAR(64) NOT NULL,
     email    VARCHAR(30) NOT NULL UNIQUE,
     role     VARCHAR(15) NOT NULL,
     cityID   INT4 NOT NULL,
     PRIMARY KEY (userID)
  );

CREATE TABLE event
  (
     eventID            INT4 NOT NULL,
     eventName          VARCHAR(255) NOT NULL,
     eventDate          DATE,
     eventTime          TIME(4),
     localizationID     INT4 NOT NULL,
     organizerID        INT4 NOT NULL,
     festivalID INT4,
     PRIMARY KEY (eventID)
  );

CREATE TABLE piece
  (
     pieceID     INT4 NOT NULL,
     pieceLength INT4,
     genreName   VARCHAR(50) NOT NULL,
     artistID    INT4 NOT NULL,
     PRIMARY KEY (pieceID)
  );

CREATE TABLE genre
  (
     genreName VARCHAR(50) NOT NULL,
     PRIMARY KEY (genrename)
  );

CREATE TABLE country
  (
     countryName VARCHAR(60) NOT NULL,
     PRIMARY KEY (countryname)
  );

CREATE TABLE ticketvendor
  (
     ticketVendorName VARCHAR(255) NOT NULL,
     ticketVendorPage VARCHAR(255) NOT NULL,
     PRIMARY KEY (ticketvendorname)
  );

CREATE TABLE organizer
  (
     organizerID   INT4 NOT NULL,
     organizerName VARCHAR(255) NOT NULL,
     organizerPage VARCHAR(255),
     PRIMARY KEY (organizerID)
  );

CREATE TABLE city
  (
     cityID      INT4 NOT NULL,
     cityName    VARCHAR(75) NOT NULL,
     countryName VARCHAR(60) NOT NULL,
     PRIMARY KEY (cityID)
  );

CREATE TABLE profession
  (
     professionName VARCHAR(50) NOT NULL,
     PRIMARY KEY (professionname)
  );

CREATE TABLE artist
  (
     artistID       INT4 NOT NULL,
     artistName     VARCHAR(50) NOT NULL,
     foundationYear INT4,
     description    VARCHAR(255),
     PRIMARY KEY (artistID)
  );

CREATE TABLE performance
  (
     eventID  INT4 NOT NULL,
     artistID INT4 NOT NULL,
     PRIMARY KEY (eventID, artistID)
  );

CREATE TABLE "having"
  (
     artistID       INT4 NOT NULL,
     professionName VARCHAR(50) NOT NULL,
     PRIMARY KEY (artistID, professionName)
  );

ALTER TABLE "user"
  ADD CONSTRAINT fkuser826554 FOREIGN KEY (cityID) REFERENCES city (cityID);

ALTER TABLE event
  ADD CONSTRAINT fkevent744903 FOREIGN KEY (localizationID) REFERENCES
  localization (localizationID);

ALTER TABLE ticket
  ADD CONSTRAINT fkticket454186 FOREIGN KEY (eventID) REFERENCES event (eventID)
;

ALTER TABLE event
  ADD CONSTRAINT fkevent773744 FOREIGN KEY (festivalID) REFERENCES
  festival (festivalID);

ALTER TABLE ticket
  ADD CONSTRAINT fkticket742600 FOREIGN KEY (ticketVendorName) REFERENCES
  ticketvendor (ticketVendorName);

ALTER TABLE event
  ADD CONSTRAINT fkevent164652 FOREIGN KEY (organizerID) REFERENCES organizer (
  organizerID);

ALTER TABLE piece
  ADD CONSTRAINT fkpiece653119 FOREIGN KEY (artistID) REFERENCES artist (
  artistID);

ALTER TABLE piece
  ADD CONSTRAINT fkpiece858124 FOREIGN KEY (genrename) REFERENCES genre (
  genrename);

ALTER TABLE performance
  ADD CONSTRAINT fkperformanc121395 FOREIGN KEY (eventID) REFERENCES event (
  eventID);

ALTER TABLE performance
  ADD CONSTRAINT fkperformanc282927 FOREIGN KEY (artistID) REFERENCES artist (
  artistID);

ALTER TABLE "having"
  ADD CONSTRAINT fkhaving310061 FOREIGN KEY (professionName) REFERENCES
  profession (professionname);

ALTER TABLE "having"
  ADD CONSTRAINT fkhaving739124 FOREIGN KEY (artistID) REFERENCES artist (
  artistID);

ALTER TABLE localization
  ADD CONSTRAINT fklocalizati158647 FOREIGN KEY (cityID) REFERENCES city (cityID
  );

ALTER TABLE city
  ADD CONSTRAINT fkcity151493 FOREIGN KEY (countryName) REFERENCES country (
  countryname); 