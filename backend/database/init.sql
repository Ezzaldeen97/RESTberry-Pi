CREATE DATABASE IF NOT EXISTS QAIA_DB;
CREATE TABLE IF NOT EXISTS Arrivals(
airline varchar(25) NOT NULL,
origin varchar(20) NOT NULL,
Flight_number varchar(10) NOT NULL,
scheduled_time datetime NOT NULL,
estimated_time datetime NOT NULL,
gate VARCHAR(5),
flight_status varchar(20),
PRIMARY KEY (scheduled_time, Flight_number)

);

CREATE TABLE IF NOT EXISTS Departures(
airline varchar(25) NOT NULL,
destination varchar(20) NOT NULL,
Flight_number varchar(10) NOT NULL,
scheduled_time datetime NOT NULL,
estimated_time datetime NOT NULL,
gate VARCHAR(5),
flight_status varchar(20),
PRIMARY KEY (scheduled_time, Flight_number)

);