import os
import json
import psycopg2
import sql_queries as sq


with psycopg2.connect(dbname='sparkifydb', user='student', 
			password='student', host='localhost') as conn:
	with conn.cursor() as cur:
		cur.execute("drop table if exists song_db;")
		cur.execute(sq.create_song_db)
		for folder, sub, files in os.walk('data\\song_data'):
			for file in files:
				with open(folder + os.sep + file, 'r') as f:
					for line in f:
						line = json.loads(line)
						values = [line['artist_id'], line['artist_location'], line['artist_latitude'],
									line['artist_longitude'], line['artist_name'], line['duration'],
									line['num_songs'], line['song_id'], line['title'],
									line['year']]
						cur.execute(sq.insert_into_song, values)