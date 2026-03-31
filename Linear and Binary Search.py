def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):     #incase of the binary searcghh the array should be sorted
    arr.sort()  # Sort the array before performing binary search
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1   

def main():
    arr = []
    n = int(input("Enter the number of elements: "))
    i = 0
    while i < n:
        try:
            element = int(input(f"Enter element {i + 1}: "))
            if element in arr:
                print("Duplicate element! Please enter a unique element.")
                continue
            if element < 0:
                print("Negative element! Please enter a non-negative element.")
                continue
            arr.append(element)
            i += 1  # Only increment when a valid element is added
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
    
    try:
        key = int(input("Enter the key to search: "))
    except ValueError:
        print("Invalid key! Please enter a valid integer.")
        return
    
    print("\nPress 1. Linear Search")
    print("Press 2. Binary Search")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    if choice == 1:
        result = linear_search(arr, key)
    elif choice == 2:
        result = binary_search(arr, key)
    else:
        print("Invalid choice!")
        return
    if result != -1:
        print(f"Element found at index : {result}")
    else:
        print("Element not found")
        

if __name__ == "__main__":
    main()