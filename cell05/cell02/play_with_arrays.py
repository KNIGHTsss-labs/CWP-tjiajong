arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []
for i in range(len(arr1)):
    if arr1[i] > 5:
        arr1[i] += 2
        arr2.append(arr1[i])
print(arr2)