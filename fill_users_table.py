import os
import json
import psycopg2
import sql_queries as sq


def fill_user_data(cur, folderpath):
	for folder, sub, files in os.walk(folderpath):
			for file in files:
				with open(folder + os.sep + file, 'r') as f:
					for line in f:
						line = json.loads(line)
						if line['userId']:
							values = [line['userId'], line['firstName'], 
									line['lastName'], line['gender'], 
									line['level']]
							cur.execute(sq.insert_into_users, values)
							

def main():
	conn = psycopg2.connect(dbname='sparkifydb', user='student', 
				password='student', host='localhost')
	cur = conn.cursor()				
	cur.execute("drop table if exists users;")
	cur.execute(sq.create_users_table)
	fill_user_data(cur, "data\\log_data")
	conn.commit()
	conn.close()

main()	