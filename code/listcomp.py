li = [3, 2, 4, 1]
nested_li = [ elem_1 * 2 for elem_1 in
    [it + 1 for it in li]
]
print(nested_li)




#li = [1, 2, 3, 4, 6]
# new_li = [2, 4, 6, 8, 12]

#new_li = [item * 2 for item in li if item > 3]

# for item in li:
#     new_li.append(item*2)

# c = 0
# while c < len(li):
#     new_li.append(li[c] * 2)
#     c += 1
#
# print(new_li)