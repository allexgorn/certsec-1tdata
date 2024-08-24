#Скрипт Python для генерацит синтетических данных для СУБД Postgres

from random import choice, randint
import os

first_names = ["Alexander", "Dmitry", "Sergey", "Konstantin", "Kirill", "Maxim", "Alexey", "Igor", "Yuri", "Stepan"]
last_names = ["Karavaev", "Sokolov", "Smirnov", "Sekushin", "Gerasimov", "Ivanov", "Kolotilov", "Gorbunov", "Efimov", "Kulnevsky"]
cities = ["Moscow", "Saint Petersburg", "Vologda", "Ekaterinburg", "Nizhny Novgorod", "Novosibirsk", "Kazan", "Chelyabinsk", "Omsk", "Samara"]

persons = []

os.system("touch init.sql")

createTableSQL = "CREATE TABLE IF NOT EXISTS test_table (name VARCHAR(10) NOT NULL, surname VARCHAR(15) NOT NULL, city VARCHAR(20) NOT NULL, age INTEGER NOT NULL);"

with open('init.sql', 'a') as file:
    file.write(createTableSQL + "\n")

for __ in range(0, 201):
    first_name = choice(first_names)
    last_name = choice(last_names)
    city = choice(cities)
    age = randint(1, 150)

    persons.append({"name": first_name, "surname": last_name, "city": city, "age": age})

for i in range(0, 201):
    if persons[i]["age"] % 2:
        continue
    else:
        insertValueSQL = f"INSERT INTO test_table (name, surname, city, age) VALUES ('{persons[i]['name']}', '{persons[i]['surname']}', '{persons[i]['city']}', {persons[i]['age']});"
        with open('init.sql', 'a') as file:
            file.write(insertValueSQL + "\n")

