--user

--find user in table:
SELECT user_id, is_deleted FROM statbot.users
WHERE user_id = {user_id};
--if no:
INSERT INTO statbot.users (user_id)
VALUES ({user_id});

--update language:
SELECT * FROM statbot.laguages
WHERE lang_id = {lang_id};

UPDATE statbot.users
SET lang_id = {lang_id};

--update firstname
UPDATE statbot.users
SET firstname = '{firstname}';

--get user main info
SELECT user_id, lang_id, firstname, is_deleted FROM statbot.users;

--metric

--new metric
SELECT * FROM metric_names
WHERE metric_name = '{metric_name}';
--if no:
INSERT INTO metric_names (metric_name, creator_id, descr)
VALUES ('{metric_name}', {user_id}, '{descr}');

--get all availible metrics
SELECT * FROM metric_names
WHERE is_actual = 1;

--notifications

--get current
SELECT user_id, metric_id, call_id, call_time FROM user_time_pref
WHERE user_id = {user_id} AND is_deleted = 0;

--set new
INSERT INTO user_time_pref (user_id, metric_id, call_id, call_time )
VALUES ({user_id}, {metric_id}, {call_id}, {call_time});

--stats

--add row
INSERT INTO metrics (user_id, metric_id, value, type_code)
VALUES ({user_id}, {metric_id}, {value}, {type_code});

--get stats
SELECT value, load_ts FROM metrics
WHERE user_id = {user_id} AND metric_id = {metric_id};