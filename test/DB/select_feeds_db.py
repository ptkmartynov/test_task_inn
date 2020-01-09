import psycopg2

con = psycopg2.connect(
    database="postgres",
    user="pt_system",
    password="P@ssw0rdP@ssw0rd",
    host="grafin-zeus.rd.ptsecurity.ru",
    port="5432"
)

print("Database opened successfully")
cursor = con.cursor()

cursor.execute("SELECT * FROM sp_antifraud.public.feed_value where type = 'inn'")
#cursor.execute("SELECT * FROM public.feed_value where type = 'inn'")
records = cursor.fetchall()

for row in cursor:
    print("INN = ", row)

print("Operation done successfully")
con.close()