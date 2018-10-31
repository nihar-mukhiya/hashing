list1 = []
size = int(input("enter the size of hash table"))
size = size + size
for j in range(size + 1):
    list1.insert(j, None)

inputter1 = int(input('number of elements to be inserted'))
for i in range(inputter1):
    inputter = int(input("enter the element: "))
    ind = inputter % size
    if list1[ind] is None:
        list1[ind] = inputter
    else:
        while list1[ind] is not None:
            global next_ind
            ind = ind + 1
            next_ind = ind

        list1[next_ind] = inputter
list1.remove(list1[-1])
print(list1)