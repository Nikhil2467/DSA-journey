#1. Traversal (Printing all elements)
print("\n Traversal of Array:")
for i in arr:
  print(i)

#2. Insertion (insert element at a position) 
element = 25
position = 2 # index where you want to insert

arr.insert(position, element)

print("\n After Insertion:", arr)

#3. Deletion (remove element)
arr.remove(30) # removes first occurrence of 30 
print("\n After Deletion (by value):",arr)

#4. Searching (Linear Search)
key = 40
found = False

for i in range(len(arr)):
  if arr[i] == key:
    print("\nElement found at index:",i)
    found = True
    break

if not found:
  print("n\Element not found")



#5. Find the maximum element in array

arr = [10,20,30,40,15]

max_val = arr[0]

for i in arr:
  if i > max_val:
    max_val = i

print("Maximum:", max_val)

#6. Sum of array element
total = 0

for i in arr:
  total = total + i 

print("Sum:", total)
