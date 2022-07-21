if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

i = [ a for a in range(x+1) ]
j = [ a for a in range(y+1) ]
k = [ a for a in range(z+1) ]

result = [[c,d,e] for c in i for d in j for e in k]

final_result = [item for item in result if sum(item)!=n]

# final_result2 = [ item for item in [[c,d,e] for c in i for d in j for e in k] if sum(item)!=n ]

# final_result2 = [[c,d,e] for c in i for d in j for e in k if sum([c,d,e])!=n]

print(final_result)

        
