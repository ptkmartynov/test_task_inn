import psycopg2

con = psycopg2.connect(
    dbname="sp_antifraud",
    user="pt_system",
    password="P@ssw0rdP@ssw0rd",
    host="grafin-zeus.rd.ptsecurity.ru",
    port="5432"
)

testinn = str("114226111190")

print("Database opened successfully")
cursor = con.cursor()

cursor.execute("SELECT value FROM public.feed_value where type = 'inn'")
records = cursor.fetchall()

for i in records:
    if testinn in i:
        print("yes", testinn, i)
        break
if testinn not in i:
    print('no data')

print("Operation done successfully")
con.close()
