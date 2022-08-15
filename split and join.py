def split_and_join(line):
    x = line.split()
    new_line = '-'.join(x)
    return new_line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)