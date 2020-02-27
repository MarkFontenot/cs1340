# Bubble sort
def bubble_sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

a_list = [34, 1, 2, 10, 12, 9]
bubble_sort(a_list)
print(a_list)