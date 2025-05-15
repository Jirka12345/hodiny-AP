#arr = list(range(1,1000))
#print(arr) - vyplní pole od 1 do 1000

arr = []
for i in range(10):
    arr.append(i)
print(arr)
a = 3
b = 8
"""pom = arr[a]
arr[a] = arr[b]
arr[b] = pom
print(arr)"""

arr[a], arr[b] = arr[b], arr[a]
print(arr)