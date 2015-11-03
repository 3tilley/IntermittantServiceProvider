CREATE TABLE ping(
    timestamp       MEDIUMINT,
    host            INT,
    iswifi          BOOLEAN,
    count           INTEGER,
    lost            INTEGER,
    min             DOUBLE,
    max             DOUBLE,
    mean            DOUBLE,
    median          DOUBLE,
    stdev           DOUBLE,
    countabove25    INT,
    countabove50    INT,
    countabove75    INT,
    countabove100   INT
);

CREATE TABLE target(
    hostkey     INT,
    hostaddress VARCHAR(50)
);

INSERT INTO target VALUES(1, 'www.google.com');
INSERT INTO target VALUES(2, '216.58.208.68');
INSERT INTO target VALUES(3, 'home.bt.com');
INSERT INTO target VALUES(4, '178.79.201.80');

