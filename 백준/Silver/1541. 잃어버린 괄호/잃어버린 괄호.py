import sys


nn = sys.stdin.readline().strip()

nnn = nn.split('-')

result = sum(map(int, nnn[0].split('+')))

for part in nnn[1:]:
    result -= sum(map(int, part.split('+')))


print(result)