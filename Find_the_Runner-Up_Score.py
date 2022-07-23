if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)

biggest = -100
for item in arr:
    if item>biggest:
        biggest = item
arr2 = [ item for item in arr if item !=biggest ]
runner = -100
for item in arr2:
    if item > runner:
        runner = item

print(runner)
