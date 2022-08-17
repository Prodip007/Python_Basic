N, M = map(int, input().split())

for i in range(N//2):
    print(((i+i+1)*'.|.').center(M, '-'))

print('WELCOME'.center(M, '-'))
for i in range(N//2-1, -1, -1):
    print(((i+i+1)*'.|.').center(M, '-'))