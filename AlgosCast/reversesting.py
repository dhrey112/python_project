import string


def reverse_string(str_: string):
    reserved = ''
    for i in str_:
        reserved = i + reserved
    return reserved


def user_input():
    try:
        input_ = input("Enter string: ")
    except Exception:
        if input_ != reverse_string():
            print("Error")
    print(reverse_string(input_))


user_input()
