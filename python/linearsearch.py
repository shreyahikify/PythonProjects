def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

items = ["apple", "banana", "cherry", "date"]
target = input("Enter item to search for: ")

result = linear_search(items, target)
if result != -1:
    print(f"Item found at index {result}")
else:
    print("Item not found.")