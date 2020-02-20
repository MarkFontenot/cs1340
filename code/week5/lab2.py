# with open("GOOG.csv", "r") as the_file:
#     data = the_file.readlines()
#
#
# second_row = data[1].split(",")
# dates = second_row[0].split("-")
# print(dates[1])


ls_2d = [
    [1, 2, 3, 4],
    [10, 22, 98],
    [10, 1, -1]
]

def get_sum_starts_10(l, num):
    total = 0
    for r in l:
        if r[0] == num:
            total += sum(r)
    return total

total = get_sum_starts_10(ls_2d, 1)
print(total)