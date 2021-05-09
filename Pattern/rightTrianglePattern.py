# # TODO      *
# #         * *
# #       * * *
# #     * * * *
# #   * * * * *
#
# length = 5
# for i in range(length):
#     for j in range(length - 1):
#         print(" ", end="")
#         for j in range(i):
#             print("*", end="")
#     print()


import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')