# # Literals or Values
#
# "this is a string"
#
# 'this is also a string'
#
# """
# this is the first line
# second line
# another line
# """
#
# 9
#
# 3.14
#
# True
# False
#
#
# message = "this IS A STR"
# name = "xinyi"
#
# print(message)
# print(name)
#
#
# price_per_mile = 0.25
# number_days = 3
#
# amount = number_days * price_per_mile
# print(amount)


# Sequence data type

# Tuple, list, string

# a_tuple = ("name", 22, "cs")
#
# a_list = ["name", 22, "cs"]
#
# a_list[0] = "carl"
# print(a_list[:3])

# a_dict = {}
#
# a_dict["name"] = 22
# a_dict["age"] = "xinyi"
# a_dict["address"] = {"zip": 75206,
#                      "apt": 123}
#
# a_list = [1, 2, 3, 4,23,45,6,9, 3]

# customer_code = 'B'
#
# num_days = 3
#
# if customer_code == 'B':
#     amount = num_days * 0.25
#     print(amount)
# elif customer_code == 'D':
#     print("do something else")
# elif customer_code == 'C':
#     print("something else")
# else:
#     print("default option")

# a_list = [1, 3]
# counter = 0
#
# while a_list:
#     code = input("Customer code:")
#     if code == 'Q' or code == 'q':
#         break
#     else:
#         print("do the calculation")
#
# print("Thank you for uising this program")

# names = ["carl", "xinyi", "david"]
#
# while names:
#     print("checking in guest:", names[0])
#     del names[0]
#     print(names)

a_list = [9, 1, 10, 3, 6]
#
# def get_sum(l):
#     total = 0
#     for i in l:
#         total += i
#     return total
#
# def print_massgae(amount_due, days):
#     print("amount due:", amount_due)
#     print("number of days:", days)

# for num in a_list:
#     print(num)
#
#
# while True:
#     print("do something")

# def a_function(age, name):
#     print("this function return the sum of two numbers")
#     print(age)
#     print(name)
#
# print("this will be printed first")
# print(a_function(name="xinyi", age=22))

a_list = [5, 2, 3]
#print(sum(a_list))

new_list = sorted(a_list)
print(new_list)