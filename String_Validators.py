if __name__ == '__main__':
    s = input()

    has_alphanumeric = False
    has_alphabetical = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    for char in s:
        if char.isalnum():
            has_alphanumeric = True
            if char.isdigit():
                has_digits = True
            else:
                has_alphabetical = True
                if char.isupper():
                    has_uppercase = True
                else:
                    has_lowercase = True

print(has_alphanumeric)
print(has_alphabetical)
print(has_digits)
print(has_lowercase)
print(has_uppercase)