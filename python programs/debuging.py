#import pdb;pdb.set_trace()
#breakpoint() works same as pdb
marks = int(input("enter your marks : "))
#breakpoint()#different result from the two in line 1and 2
if marks >= 70:
    grade ="A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40 :
    grade = "D"
elif marks < 40 and marks >70:
    grade = "F"
else:
    grade ="not in the range"
print(grade)