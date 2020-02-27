# a_2d_list = [
#     [[1], [2], [3]],
#     [[4], [5], [6]],
#     [[0], [3], [1]]
# ]
# print(a_2d_list[0][0][0])

#
# a_queue = [1, 2, 3, 4, 5]
#
# #a_queue.append()
# last_element = a_queue.pop()
# print(last_element)
#
# print(a_queue)
#a list has lengt n, n comparisons
# n / 2 comparisons

a_random_list = [1, 3]

num = 2

def search_num(ls, num):
    res = False
    for item in ls:
        if item == num:
            res = True
    return res

res = search_num(a_random_list, num)
print(res)


# num in a_random_list
# # for a in a_random_list:
# #     range()
#
# a_random_list.sort()
# # print(a_random_list)
#
# #ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ls = list(range(1, 11, 2))
# print(ls)
# #for a in range(10):
#
#
