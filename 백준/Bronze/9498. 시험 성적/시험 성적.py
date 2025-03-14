import sys


a = int(sys.stdin.readline().strip())

if 100 >= a >= 90:
    grade = 'A'
elif 90 > a >= 80:
    grade = 'B'
elif 80 > a >= 70:
    grade = 'C'
elif 70 > a >= 60:
    grade = 'D'
elif 60 > a :
    grade = 'F'

    


    
print(grade)