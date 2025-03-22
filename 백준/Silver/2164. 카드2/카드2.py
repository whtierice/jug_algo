from collections import deque

n = int(input())

deck = deque(range(1,n+1))

while len(deck) > 1:
    #앞에 쳐내기
    deck.popleft()
    #남은거 뒤로 옮기기
    temp = deck.popleft()
    deck.append(temp)


print(deck[0])
