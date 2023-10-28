import os
def new_user():
    confirm = "N"
    while confirm != "y":
        username = input("enter the name of a user to add: ")
        print("use username '" +username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser" + username)
new_user()