import os
import psycopg
import requests
import json

from dotenv import load_dotenv      # database connection

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")              # retrieve env var
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

connection = psycopg.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,               # establish connection
    password=db_password,
    port=db_port
)

cursor = connection.cursor()

user_input = input("Ask about the NASC database: ") # accept a question

cursor.execute("""
    SELECT *
    FROM ngo_swim.providers;
""")
rows = cursor.fetchall()

database_context = ""

for row in rows:        # Convert database rows into text that can be included in the Ollama prompt
    database_context += str(row) + "\n"

prompt = f"""
Use only the database information below to answer the user's question.
If the answer cannot be found in the database information, say that you do not have enough information.

Database information:
{database_context}
                            
User question:
{user_input}
"""
    # use the database conext and user input to develope a prompt for the ollama

url = "http://localhost:11434/api/chat" # api chat endpoint

messages = [        # create the message payload
    {
        "role": "user",
        "content": prompt   
    }
]

data = {        # build request data
    "model": "llama3.2",
    "messages": messages,
    "stream": False
}

response = requests.post(url, json=data) # send the data

result = response.json()    # parse the json response

print(result["message"]["content"]) # print the ollama answer