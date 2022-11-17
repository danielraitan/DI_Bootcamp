import requests
import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  '123456789'
DATABASE =  'countrys'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)

cursor = connection.cursor() 

url = 'https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population'

data = requests.get(url).json()

for i in range(1, 11):
    name = data[i]['name']['common']
    capital = data[i]['capital'][0]
    population = data[i]['population']
    q = f"INSERT INTO countrys(name, capital, population) values {name, capital, population};"
    cursor.execute(q) 
    connection.commit() 

connection.close()
