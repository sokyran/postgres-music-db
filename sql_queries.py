create_songplays = ("""
	CREATE TABLE IF NOT EXISTS songplays (
		songplay_id serial primary key,
		start_time timestamp,
		user_id varchar(10) NOT NULL,
		level varchar(10),
		song_id varchar(20),
		artist_id varchar(20),
		session_id integer,
		location varchar(255),
		user_agent varchar(255)
	);
""")

create_log_db = """
	CREATE TABLE IF NOT EXISTS log_db (
		songplay_id serial primary key,
		artist varchar,
		firstName varchar,
		lastName varchar,
		gender varchar,
		length float,
		level varchar,
		location varchar,
		song varchar,
		sessionId integer,
		userAgent varchar,
		userId varchar NOT NULL
	);
"""

insert_into_log = """
	INSERT INTO log_db(artist, firstname, lastName,
						gender, length, level, 
						location, song, sessionId,
						userAgent, userId) 
						VALUES(%s, %s, %s, 
							   %s, %s, %s, 
						 	   %s, %s, %s, 
							   %s, %s
	);
"""

create_song_db = """
	CREATE TABLE IF NOT EXISTS song_db (
		id serial PRIMARY KEY,
		artist_id varchar,
		artist_location varchar,
		artist_latitude float,
		artist_longitude float,
		artist_name varchar,
		duration float,
		num_songs integer,
		song_id varchar,
		title varchar,
		year integer
	);
"""

insert_into_song = """
	INSERT INTO song_db(artist_id, artist_location, artist_latitude,
						artist_longitude, artist_name, duration, 
						num_songs, song_id, title, 
						year) 
						VALUES(%s, %s, %s, 
							   %s, %s, %s, 
						 	   %s, %s, %s, 
							   %s
	);
"""

create_time_table = """
	CREATE TABLE IF NOT EXISTS time(
		start_time timestamp NOT NULL PRIMARY KEY,
		hour int,
		day int,
		week int,
		month int,
		year int,
		weekday varchar
	);
"""

insert_into_time = """
	INSERT INTO time(
		start_time, hour, day,
		week, month, year,
		weekday) 
		VALUES (
			%s, %s, %s,
			%s, %s, %s,
			%s) ON CONFLICT (start_time) 
				DO NOTHING;
"""


create_users_table = """
	CREATE TABLE IF NOT EXISTS users(
		user_id int NOT NULL PRIMARY KEY ,
		first_name varchar,
		last_name varchar,
		gender char,
		level varchar
	);
"""

insert_into_users = """
	INSERT INTO users(
		user_id, first_name, last_name, gender, level)
		VALUES (%s, %s, %s, %s, %s)
		ON CONFLICT (user_id) DO UPDATE
			set first_name = EXCLUDED.first_name,
			last_name = EXCLUDED.last_name,
			gender = EXCLUDED.gender,
			level = EXCLUDED.level;
"""