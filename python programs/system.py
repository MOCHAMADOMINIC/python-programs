import os
print(os.getcwd()) # current working directly
print(os.getlogin()) # returns the name of logged in user
#os.mkdir('folder1')
print(os.listdir()) # list the content of current directory
#print(os.system(command= "pip install django"))  #to run commands in a subshell of the system
#os.chown("my file.txt") #change ownership of a file
os.chmod("my file.txt",mode= 477) #change  the access permission of a file
print(os.getenv(key="pycharm"))
print(os.getpid())
#print(os.getgroups())
#print(os.getgrouplist())
os.system("whoami")
#os.system("dom")
os.system("powershell.exe")

