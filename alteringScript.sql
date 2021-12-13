CREATE TYPE currencies AS ENUM ('EUR', 'PLN', 'USD', 'CAD', 'AUD');
CREATE TYPE participationOptions AS ENUM ('Going', 'Not Going', 'Interested', 'Not interested', 'I have taken part', 'I have not taken part');

ALTER TABLE tickets
ADD COLUMN currency currencies;

CREATE TABLE user_event
  (
     eventID         INT4 NOT NULL,
     userID          INT4 NOT NULL,
     participation   participationOptions,   
     PRIMARY KEY (eventID, userID)
  );

ALTER TABLE user_event
ADD CONSTRAINT user_event_event FOREIGN KEY (eventID) REFERENCES
events (eventID);

ALTER TABLE user_event
ADD CONSTRAINT user_event_user FOREIGN KEY (userID) REFERENCES users (
userID);

CREATE TABLE user_genre
(
    userID INT4 NOT NULL,
    genreID INT4 NOT NULL,
    PRIMARY KEY (userID, genreID)
);

ALTER TABLE user_genre
ADD CONSTRAINT user_genre_genre FOREIGN KEY (genreID) REFERENCES
genres (genreID);

ALTER TABLE user_genre
ADD CONSTRAINT user_genre_user FOREIGN KEY (userID) REFERENCES users (
userID);