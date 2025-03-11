import random

def createArr(member): #random member to arrays
    for i in range(member):
        num = random.randint(1, 100)
        arr.append(num)

arr = []
createArr(10)
print(f"original array: {arr} \n")

'''bubble sort algorithm'''
n = len(arr)
count = 0 #unnessesarry
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1 #unnessesarry
            print(f"processing round({count}) :{arr}")
'''bubble sort algorithm'''

print(f"\nSorted array:    {arr}")