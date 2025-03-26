import sys


# reps = int(sys.stdin.readline().strip())

# for i in range(reps):
#     strr = list(sys.stdin.readline().strip())

#     status = True

#     while status:
#         if len(strr) == 0:
#             status = True
#             break
#         elif len(strr) < 2:
#             status = False
#             break
#         for i in range (len(strr)-1):
#             if strr[i] == '(' and strr[i+1] == ')':
#                 del strr[i:i+2]
#                 status = True
#                 break
#             else:
#                 status = False


#     if status:
#         print('YES')
#     else:
#         print('NO')


reps = int(sys.stdin.readline().strip())


for i in range(reps):
    stk = []
    brk = list(sys.stdin.readline().strip())

    for j in brk:
        if j == '(':
            stk.append(j)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(j)
    

    if stk:
        print('NO')
    else:
        print('YES')



        


