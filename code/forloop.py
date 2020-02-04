# import numpy

num_list = [2, 5, 6, 7, 8]
# total = 0
#
# for _ in num_list:
#     # print(_)
#     total += _
#     print(total)

# total = sum(num_list)
# print(total)

# total = 0
# counter = 0
# while counter < len(num_list):
#     total += num_list[counter]
#     counter += 1
#
# print(total)


a_list = [3, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list_2 = range(1, 11)
# print(list_2)
# for a in list(range(1, 11)):
#     print(a)
for _ in a_list:
    print(_)

print("+++++++++")
for i, num in enumerate(a_list):
    print(i, num)