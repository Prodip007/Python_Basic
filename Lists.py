if __name__ == '__main__':
    N = int(input())

command_list = []
for x in range(N):
    command = input()
    command_list.append(command)

command_list_stripped  = []

for item in command_list:
    x = item.split()
    command_list_stripped.append(x)

arr = []
for item in command_list_stripped:
    if len(item) == 1:
        if item[0] == 'print':
            print(arr)
        elif item[0] == 'sort':
            arr.sort()
        elif item[0] == 'pop':
            arr.pop()
        elif item[0] == 'reverse':
            arr.reverse()
        else:
            arr.append('Not a valid method 1')
    elif len(item) == 2:
        if item[0] == 'remove':
            if int(item[1]) in arr:
                arr.remove(int(item[1]))
        elif item[0] == 'append':
            arr.append(int(item[1]))
        else:
            arr.append('Not a valid method 2')
    elif len(item) == 3:
        arr.insert(int(item[1]), int(item[2]))
    else:
        arr.append('Out of the scope')