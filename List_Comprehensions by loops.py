if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

i = [ a for a in range(x+1) ]
j = [ a for a in range(y+1) ]
k = [ a for a in range(z+1) ]

result = []

for item in i:
    for things in j:
        for matter in k:
            result.append([item, things, matter])

for item in result:
    sum = 0
    for things in item:
        sum = sum + things
    if sum == n:
        result.remove(item)

print(result)


        
