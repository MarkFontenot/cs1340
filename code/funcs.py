# li = [1, 2, 3, 4, 5]
#
# # total = 0
# # for item in li:
# #     total += item
# #
# # print(total)
#
# # total = 0
# li_2 = [10, 11, 3]
# # for item in li_2:
# #     total += item
# # print(total)
#
def get_sum(li):
    """
    calculate the sum of a li
    """
    total = 0
    for item in li:
        total += item
    return total

# total = get_sum(li)
# print(total)
# total = get_sum(li_2)
# print(total)
#
# total = sum(li_2)
# print(total)
# int()
# str()
# range()
# enumerate()

# def greetings(username='DAVID', employee_id):
#     """
#     Print some greeting messages
#     """
#     print("hello")
#     print("welcome", username.lower())
#     print("Your employee id is ", employee_id)
#
# greetings(99)_
def make_pizza(*toppings):
    for _ in toppings:
        print(_)

make_pizza('onion')
