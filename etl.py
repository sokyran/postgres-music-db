import os
import json
import psycopg2
from datetime import datetime
import sql_queries as sq


def deal_with_ts(ts):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date = datetime.fromtimestamp(ts/1000.0)
    start_time = date.strftime("%Y-%m-%d %H:%M:%S")
    hour = date.hour
    day = date.day
    week = date.isocalendar()[1]
    month = date.month
    year = date.year
    weekday = weekdays[date.weekday()]
    return (start_time, hour, day, month, year, week, weekday)


def process_log_file(cur, folderpath):
	for folder, sub, files in os.walk(folderpath):
			for file in files:
				with open(folder + os.sep + file, 'r') as f:
					for line in f:
						line = json.loads(line)
						if line['userId']:
							user_values = [line['userId'], line['firstName'], line['lastName'], line['gender'], line['level']]
							cur.execute(sq.insert_into_users, user_values)

						if line['page'] == 'NextSong':
								values = deal_with_ts(line['ts'])
								cur.execute(sq.insert_into_time, values)

						cur.execute(sq.select_song_artist, (line['artist'], line['song']))
						results = cur.fetchone()
						if results:
							song_id, artist_id = results
						else:
							song_id, artist_id = None, None

						date = datetime.fromtimestamp(line['ts']/1000.0)
						start_time = date.strftime("%Y-%m-%d %H:%M:%S")
						values = [start_time, line['userId'], line['level'], song_id, artist_id, 
									line['sessionId'], line['location'], line['userAgent']]
						cur.execute(sq.insert_into_songplays, values)							


def process_song_file(cur, folderpath):
	for folder, sub, files in os.walk(folderpath):
				for file in files:
					with open(folder + os.sep + file, 'r') as f:
						lines = json.load(f)
						song_values = [lines['song_id'], lines['title'], lines['artist_id'], lines['year'], lines['duration']]
						artist_values = [lines['artist_id'], lines['artist_name'], lines['artist_location'], 
										lines['artist_latitude'], lines['artist_longitude']]
						cur.execute(sq.insert_into_songs, song_values)
						cur.execute(sq.insert_into_artists, artist_values)							


def main():
	conn = psycopg2.connect(dbname='sparkifydb', user='student', 
			password='student', host='localhost')
	cur = conn.cursor()

	process_song_file(cur, 'data\\song_data')
	process_log_file(cur, 'data\\log_data')

	conn.commit()
	conn.close()


main()