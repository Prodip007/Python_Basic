def mutate_string(string, position, character):
    line = string
    line1 = line[:position]
    line2 = line[position+1:]
    return line1 + character + line2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)