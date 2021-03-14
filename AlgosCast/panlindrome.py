def panlindrome(str_):
    reversed = ''
    for char in str_:
        reversed = char + reversed

    return reversed == str_


def user_input():
    input_ = input("Enter input: ")
    print(panlindrome(input_))


user_input()
