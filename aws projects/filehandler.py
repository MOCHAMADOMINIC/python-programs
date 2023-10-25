f = open('my file.txt', 'r')
print(f.read())
f.close()
############# overwite a file And append
f = open('my file.txt', 'a') # w ovewrites
f.write('\nloves trojan')
f.close()
