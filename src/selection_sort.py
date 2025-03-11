import random
from idlelib.colorizer import prog_group_name_to_tag


def createArr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)

arr = []
createArr(10)

print(f"Original arrays: {arr} \n")

'''selection sort'''
n = len(arr)
count = 0 #unnessesarry
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    min_value = arr.pop(min_index)
    arr.insert(i, min_value)
    count += 1 #unnessesarry
    print(f"processing rount({count}):{arr}")
'''selection sort'''

print(f"\nSorted array: {arr}")