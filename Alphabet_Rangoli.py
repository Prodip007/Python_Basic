def print_rangoli(size):

    all_letters = []

    main_chars = (size*2)-1
    total_chars = main_chars + (main_chars-1)  

    for i in range(size-1, -1, -1):
        # print(i)
        all_letters.append(chr(ord('a')+i))
        if len(all_letters)>1:
            line1 = all_letters + list(reversed(all_letters[:-1]))
            main_line = '-'.join(line1)
            print(main_line.center(total_chars, '-'))
        else:
            main_line = '-'.join(all_letters)
            print(main_line.center(total_chars, '-'))
    
    for i in range(size-1, 0, -1):
        all_letters.pop()
        if len(all_letters)>1:
            line1 = all_letters + list(reversed(all_letters[:-1]))
            main_line = '-'.join(line1)
            print(main_line.center(total_chars, '-'))
        else:
            main_line = '-'.join(all_letters)
            print(main_line.center(total_chars, '-'))


    

    # line = list(reversed(all_letters[1:])) + all_letters

    # main_line = '-'.join(line)

    # i = 0
    # for item in line:
    #     line_length = len(line) + len(line) - 1
    #     i = i+1
    #     print(item.center(line_length,'-'))
    #     print(i, item, main_line)

    
    # for line2 in main_line:
    #     print(main_line)

    
    # print(main_line)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)