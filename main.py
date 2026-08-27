#Caleb Close
# 8/25/26
# API Practice 

import requests     #importing the requests Library 

url = "http://localhost:11434/api/chat" #Local Host on my computer with the API listening on port 11434

messages = []   #List for conversation memory 

while True:     #While loop to allow for continuous questions
    user_input = input("Question: ")    #Take user input for question 

    if user_input.lower() == 'exit':    #exit case
        break

    messages.append({           #Add the role and content to the messages list
        "role":"user",
        "content": user_input   

    })

    data = {        #Python Dictionary
        "model": "llama3.2",
        "messages": messages,      # Chat history stored in the dictionary key   
        "stream": False
    }


    response = requests.post(url, json = data)  #Send an HTTP POST request to url and include the contents of data as JSON.

    result = response.json()    # Get ollamas answer

    messages.append({       #add the ollama response to the chat history 
        "role":"assistant",
        "content":result["message"]["content"]
    })
    
    
    print(result["message"]["content"])    