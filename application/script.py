import psycopg2

conn = psycopg2.connect("dbname='gorbunov' user='postgres' password='postgres' host='postgres'")

cur = conn.cursor()

firstList = cur.execute("SELECT name, MIN(age) as age FROM test_table WHERE CHAR_LENGTH(name) = 6 GROUP BY name ORDER BY age ASC;")

firstList = cur.fetchall()

if firstList:
    print("Минимальный возраст по длине имени из 6 символов")
    for item in firstList:
        print(f"Имя: {item[0]}\nВозраст: {item[1]}\n\n")


secondList = cur.execute("SELECT name, MAX(age) as age FROM test_table WHERE CHAR_LENGTH(name) = 6 GROUP BY name ORDER BY age ASC;")

secondList = cur.fetchall()

if secondList:
    print("Максимальный возраст по длине имени из 6 символов:")
    for item in secondList:
        print(f"Имя: {item[0]}\nВозраст: {item[1]}\n\n")

