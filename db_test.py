import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")              # Gets the information stored in the .env file
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

print("Host:", db_host)
print("Database:", db_name)
print("User:", db_user)
print("Password found:", db_password is not None)
print("Port:", db_port)

connection = psycopg.connect(   # Database connection without revealing sensitive data
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)

print("Successfully connected to PostgreSQL!")

cursor = connection.cursor()
cursor.execute("SELECT * FROM ngo_swim.providers;")     #
rows = cursor.fetchall()    # get all the rows from the previous query 

for row in rows:    # loop through database rows
    print(row)

cursor.close()
connection.close()