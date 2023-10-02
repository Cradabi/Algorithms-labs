arr=[1,2,3,4,5,6,7,8,9]
arr1=arr
for i in range(len(arr)):
    arr1[i]=arr1[i]**0.5
print(arr1)
arr1=arr
for i in range(len(arr)):
    arr1[i]=arr1[i]**2
print(arr1)
arr1=arr
for i in range(len(arr)):
    arr1[i]=arr1[i]**3
print(arr1)
