list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6]
result = []
for x in list1:
    if x not in list2:
        result.append(x)
print(result)
