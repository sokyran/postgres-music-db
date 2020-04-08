import os
import json
import psycopg2
import datetime
import sql_queries as sq


def deal_with_ts(ts):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date = datetime.datetime.fromtimestamp(ts/1000.0)
    start_time = date.strftime("%Y-%m-%d %H:%M:%S")
    hour = date.hour
    day = date.day
    week = date.isocalendar()[1]
    month = date.month
    year = date.year
    weekday = weekdays[date.weekday()]
    return (start_time, hour, day, month, year, week, weekday)


def fill_time_data(cur, folderpath):
	for folder, sub, files in os.walk(folderpath):
				for file in files:
					with open(folder + os.sep + file, 'r') as f:
						for line in f:
							line = json.loads(line)
							if line['page'] == 'NextSong':
								values = deal_with_ts(line['ts'])
								cur.execute(sq.insert_into_time, values)


def main():
	conn = psycopg2.connect(dbname='sparkifydb', user='student', 
			password='student', host='localhost')
	cur = conn.cursor()
	cur.execute("drop table if exists time;")
	cur.execute(sq.create_time_table)
	fill_time_data(cur, "data\\log_data")
	conn.commit()


main()