#my list
my_list = []

#append items to my list
my_list.extend([10,20,30,40])

#insert the valu 15
my_list.insert(1, 15)

#extend the list
my_list.extend([50, 60, 70])

#remove the last element from my list
my_list.pop()

#sort my list
my_list.sort()

#find and print the list
index_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_30)
