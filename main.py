#Caleb Close
# 8/25/26
# API Practice 

import requests     #importing the requests Library 

url = "http://localhost:11434/api/generate" #Local Host on my computer with the API listening on port 11434

user_input = input("Question: ")    #Take user input for question 

data = {        #Python Dictionary
    "model": "llama3.2",
    "prompt": user_input,
    "stream": True
}


response = requests.post(url, json = data)  #Send an HTTP POST request to url and include the contents of data as JSON.

result = response.json()
print(result["response"])