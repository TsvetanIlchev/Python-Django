# Lists

# mylist = [1, 2, 3]
# mylist = ["asdas", 1, 2, 3, True, [1,2,3]]
# print(len(mylist))

mylist = ["a", "b", "c"]
# print(mylist[0])
# print(mylist[-1])
# print(mylist[:3])

# print("Before reassignment")
# print(mylist)
# mylist[0] = "New Item"
# print("After reassignment")
# print(mylist)

# mylist.append("New Item")
# print(mylist)
# mylist.append(["x", "y", "z"])
# print(mylist)
# mylist_2 = ["x", "y", "z"]
# mylist.extend(mylist_2)
# print(mylist)

# item = mylist.pop(0)
# print(mylist)
# print(item)

# mylist.reverse()
# print(mylist)

# mylist_3 = ["c", "b", "a"]
# mylist_3.sort()
# print(mylist_3)

# mylist_4 = ["A", "B", ["x", "y", "z"]]
# print(mylist_4[2])
# print(mylist_4[2][1])

matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
first_col = [row[0] for row in matrix]
print(first_col)
