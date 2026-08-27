#Caleb Close
# 8/25/26
# API Practice 

import json
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
        "stream": True
    }


    response = requests.post(url, json = data, stream = True)  #send request to local server and stream response

    assistant_response = ""

    for line in response.iter_lines():      #Process Each line as it arrives
        chunk = json.loads(line)            #Convert the line from json to a python object
        content = chunk["message"]["content"]
        assistant_response += content
        print(content, end="", flush = True)    #Print the response
    
    messages.append({       #add the ollama response to the chat history 
        "role":"assistant",
        "content":assistant_response
    })
    
    print() #New line when finished 
    
    
    