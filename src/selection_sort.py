import random

def createArr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)

arr = []
createArr(10)

print(f"Original arrays: {arr} \n")
count = 0 #unnessesarry
'''selection sort'''
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    count += 1 #unnessesarry
    print(f"Processing (round {count}): {arr}") #unnessesarry
'''selection sort'''

print(f"\nSorted array: {arr}")