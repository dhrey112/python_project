
def comma_code(list_item):
    list_display = ""

    try:
        for i in range(len(list_item[:-1])):
            list_display = list_display + str(list_item[i]) + ", "
        list_display = list_display + 'and ' + str(list_item[-1])

        return list_display
    except Exception:
        return "Empty list not allowed"


fruits = ['apples', 'bananas', 'tofu', 'cats', 'grape', 'orange', 'apples']

# fruits=[]
# result = comma_code(fruits)
# print(result)

def comma_code_args(first, *rest):
    *head, final = first, *rest

    if head:
        final = f" and {final}"
        # print(final)
    return ', '.join(*head, final)

fruits = comma_code_args(fruits)
print(fruits)
