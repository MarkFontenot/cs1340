# Selection sort
def selection_sort(nlist):
   for fillslot in range(0, len(nlist)):
       min_index= fillslot
       for location in range(fillslot, len(nlist)):
           if nlist[location] < nlist[min_index]:
               min_index = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[min_index]
       nlist[min_index] = temp

a_list = [34, 1, 2, 10, 12, 9]
#selection_sort(a_list)
#print(a_list)

a_list.sort()
print(a_list)

