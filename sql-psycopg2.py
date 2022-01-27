import psycopg2


connection = psycopg2.connect(database="chinook",user="gitpod",host="127.0.0.1",port="5432")

cursor = connection.cursor()

cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Test"])

results = cursor.fetchall()


connection.close()

for result in results:
    print(result)