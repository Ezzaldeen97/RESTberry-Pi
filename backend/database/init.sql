CREATE DATABASE IF NOT EXISTS QAIA_DB;
CREATE TABLE IF NOT EXISTS Arrivals(
airline varchar(25),
origin varchar(20),
Flight_number varchar(20),
scheduled_time datetime,
estimated_time datetime,
gate INT,
flight_status varchar(10)
);

CREATE TABLE IF NOT EXISTS Departures(
airline varchar(25),
destination varchar(20),
Flight_number varchar(20),
scheduled_time datetime,
estimated_time datetime,
gate INT,
flight_status varchar(10)
);