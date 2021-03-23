import psycopg2 as pg2
conn = pg2.connect(database='dvdrental',user='postgres',password='Fifa2@11')
cur = conn.cursor()
cur.execute('select * from payment')
print(cur.fetchone())
print(cur.fetchmany(5))
print(type(cur.fetchone()))


