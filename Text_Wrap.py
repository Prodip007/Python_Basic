import textwrap

def wrap(string, max_width):
    new_string = textwrap.wrap(string, max_width)
    new_text = '\n'.join(new_string)
    return new_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)