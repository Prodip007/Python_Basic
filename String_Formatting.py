def print_formatted(number):
    decimals = []
    octals = []
    hexadecimals = []
    binaries = []
    for i in range(number):
        decimals.append(i+1)
        octals.append(f'{i+1:o}')
        hexadecimals.append(f'{i+1:x}'.upper())
        binaries.append(f'{i+1:b}')

    last_binary_length = len(binaries[len(binaries)-1])

    for i in range(len(decimals)):
        print(str(decimals[i]).rjust(last_binary_length), octals[i].rjust(
            last_binary_length), hexadecimals[i].rjust(last_binary_length), binaries[i].rjust(last_binary_length))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
