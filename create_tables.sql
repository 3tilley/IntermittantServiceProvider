CREATE TABLE ping(
    timestamp   MEDIUMINT,
    host        INT,
    iswifi      BOOLEAN,
    count       INTEGER,
    lost        INTEGER,
    min         DOUBLE,
    max         DOUBLE,
    mean        DOUBLE,
    median      DOUBLE,
    stdev       DOUBLE
);

CREATE TABLE target(
    hostkey     INT,
    hostaddress VARCHAR(50)
);

INSERT INTO target VALUES(1, 'www.google.com');

.save data.db;