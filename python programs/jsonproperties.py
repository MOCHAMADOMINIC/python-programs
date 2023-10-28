import json
filename ="username.json"
name =''
#check for a history file
try:
    with open(filename, 'r') as r:
        name = json.load(r) #load the user's name  from a history file
except IOError:
    print('first time login')
    #if user was found in the history file,welcome them  back
    if name !='':
        print("welcome ack , " + name + "! ")
    else:#if the history file doesnt exist ,ask user to enter their name
     name = input("hello! whats your name ? :")
    print("welcome, " + name + "!")
    #save the users name to the history file
try:
    with open(filename,'w')as f:
        json.dump(name,f)
except IOError:
    print("there was a problem wrinting to the history file")
