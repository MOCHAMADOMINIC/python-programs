import os


def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("enter the name of user to remove : ")
        print("remove the user: '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r" + username )
remove_user()