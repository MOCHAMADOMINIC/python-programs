num = [12, 34, 18, 48, 98, 45, 46, 65,76]
print(num[-1])#negative indexing
print(num[2:5])#slicing without step
team_chrome =["dominic","cheptoo"," cynthia" , "maryann","steve", "edwin","albert"]
print(team_chrome[-3:])
print(team_chrome[:-3])
print(num[::3]) #3steps
#print(num[1:8:2])#using start ,end and step
#print(num[::-1])#reversing a list
#num[0] = 1000 #modifying nelements in alist with new value
num[0] = num[8] #copying a value to an index
print(num)
##########list slicing
num[1:4] =[300,400,700]
print(num)
#adding elements
team_chrome.append('trojan') # adding to the last index -1
print(team_chrome)
team_chrome.insert(2,"emmanuel") # inserting to the specific index
print(team_chrome)
# removing elements
num.remove(76)# using removes
print(num)
num.pop()#removes the last element without specifying index
num.pop(2)
del num[1]
print(num)
a = "dominic"
print(a[-1])