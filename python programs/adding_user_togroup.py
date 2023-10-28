import os
import subprocess


def add_user_to_group():
    username = input("enter the name of the user that you want to add to a group :")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("the list should be separated by spaces ,for example:\r\n group1 group2 group3")
    print("the available groups are:\r\n " + output)
    chosenGroups = input("Groups: ")
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print(" Add to :")
    found = True
    groupString = ""
    for grp in chosenGroups:
      for existingGrp in output:
        if grp == existingGrp:
            found = True
            print(" - Existing group :" + grp)
            groupstring = groupstring + grp + ","
    if found == False:
        print("- New Group : " + grp )
        groupstring = groupstring + grp + ","
    else:
        found = False
        groupstring =groupstring[: -1] + " "
        confirm = ""
        while confirm != "y" and confirm != "N":
            print("add user '" + username + "' to these groups?(Y/N)" )
            confirm = input().upper()
        if confirm == "N":
            print("User '" + username + "' not added")
        elif confirm == "y":
            os.system("sudo usermod -aG" + groupString + username)
            print("user '" + username +"'  added ")
add_user_to_group()
######## run it in linux