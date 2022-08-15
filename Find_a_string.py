def count_substring(string, sub_string):
    string_length = len(string)
    sub_string_length = len(sub_string)
    count = 0

    for i in range(string_length):
        start_index = i
        end_index = i+sub_string_length
        if end_index <= string_length:
            my_sub = string[start_index : end_index]
            if my_sub == sub_string:
                count += 1   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)