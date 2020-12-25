/*
CREATE SCHEMA statbot;
*/

CREATE TABLE statbot.users 
(
	user_id int NOT NULL PRIMARY KEY,
	lang_id int NOT NULL DEFAULT (0),
	fistname varchar(128),
	is_deleted boolean NOT NULL DEFAULT false
);

CREATE TABLE statbot.languages
(
	lang_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	lang_name varchar(64) NOT NULL,
	dict varchar(2048) NOT NULL
);

CREATE TABLE statbot.metric_names
(
	metric_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	metric_name varchar(128) NOT NULL,
	creator_id int NOT NULL,
	is_actual boolean NOT NULL DEFAULT true,
	is_default boolean NOT NULL DEFAULT true
);

CREATE TABLE statbot.metrics
(
	user_id int NOT NULL,
	metric_id int NOT NULL PRIMARY KEY,
	value int NOT NULL,
	type_code int NOT NULL,
	load_ts timestamp(3) NOT NULL
);

CREATE TABLE statbot.user_time_pref
(
	user_id int NOT NULL PRIMARY KEY,
	is_default boolean DEFAULT true,
	call_id int NOT NULL,
	call_time time NOT NULL,
	is_deleted boolean DEFAULT false
);

CREATE TABLE statbot.history
(
	event_id int NOT NULL,
	user_id int NOT NULL,
	load_ts timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE statbot.events
(
	event_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	event_name varchar(64),
	description varchar(1024)
);
