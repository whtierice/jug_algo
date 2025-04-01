import sys

while True:
    stri = sys.stdin.readline()

    if not stri:
        break

    a, b, c, d = 0, 0, 0, 0
    for i in range(len(stri)):
        if 97 <= ord(stri[i]) <= 122:
            a +=1
        elif 65 <= ord(stri[i])<=90:
            b += 1
        elif ord(stri[i]) == 32:
            d +=1
        elif 48 <= ord(stri[i]) <= 57:
            c +=1

    print (a, b, c, d)

