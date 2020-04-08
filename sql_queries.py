drop_artists = "DROP TABLE IF EXISTS artists;"
drop_songs = "DROP TABLE IF EXISTS songs;"
drop_time = "DROP TABLE IF EXISTS time;"
drop_users = "DROP TABLE IF EXISTS users;"

drop_queries = [drop_artists, drop_songs, drop_time, drop_users]


create_songplays_table = """
	CREATE TABLE IF NOT EXISTS songplays(
		songplay_id serial primary key,
		start_time timestamp,
		user_id varchar NOT NULL,
		level varchar,
		song_id varchar,
		artist_id varchar,
		session_id integer,
		location varchar,
		user_agent varchar
	);
"""

insert_into_songplays = """
	INSERT INTO songplays(
		start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
		VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

create_songs_table = """
	CREATE TABLE IF NOT EXISTS songs (
		song_id varchar PRIMARY KEY,		
		title varchar,
		artist_id varchar,
		year integer,
		duration float
	);
"""

insert_into_songs = """
	INSERT INTO songs(song_id, title, artist_id, year, duration) 
				VALUES(%s, %s, %s, %s, %s)
				ON CONFLICT (song_id) DO UPDATE
					set title = EXCLUDED.title,
					artist_id = EXCLUDED.artist_id,
					year = EXCLUDED.year,
					duration = EXCLUDED.duration;
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


create_artists_table = """
	CREATE TABLE IF NOT EXISTS artists(
		artist_id varchar PRIMARY KEY,
		name varchar,
		location varchar,
		latitude float,
		longitude float
	);
"""

insert_into_artists = """
	INSERT INTO artists(artist_id, name, location, latitude, longitude)
			VALUES(%s, %s, %s, %s, %s)
			ON CONFLICT (artist_id) DO UPDATE
				set name = EXCLUDED.name,
				location = EXCLUDED.location,
				latitude = EXCLUDED.latitude,
				longitude = EXCLUDED.longitude;

"""

create_queries = [create_artists_table, create_users_table, create_songs_table, create_time_table, create_songplays_table]

select_song_artist = """
	SELECT song_id, songs.artist_id 
	FROM artists 
	JOIN songs 
	ON songs.artist_id = artists.artist_id 
	WHERE name=%s AND title=%s;
"""