import random

def createArr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)

arr = []
createArr(10)
print(f"original array (before sort): {arr}")

'''bubble sort algorithm'''
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
'''bubble sort algorithm'''

print(f"Sorted array (after sort):    {arr}")