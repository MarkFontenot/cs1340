# counter = 0
# while counter < 10:
#     counter += 1 # this is the same as counter = counter + 1
#     if counter % 2 == 1:
#         continue
#     print(counter)

names_list = ["carl", "alice", "oliva", "david"]
             # 0        1         2        3
print(names_list.index("david"))
print(len(names_list))
counter = 0
while counter < len(names_list):
    print(names_list[counter])
    counter += 1