def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]   #left will contain the elements less than the pivot
        middle = [x for x in arr if x == pivot]    #middle will contain the elements equal to the pivot
        right = [x for x in arr if x > pivot]    #right will contain the elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)   #can be assumed as the concatenation of lists
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  #Swapping without using a temporary variable
    return arr
    
#its like 
# a,b = c,d
# where a = c and b = d

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2     #to Extract the middle index
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]    #left_arr will contain the elements from left to mid (inclusive)
    right_arr = arr[mid + 1:right + 1]  #right_arr will contain the elements from mid + 1 to right (inclusive)
    i = j = 0 
    k = left     #One sub array will be merged into the original array starting from index left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:    #If the current element of left_arr is less than or equal to the current element of right_arr, it is placed in the original array at index k
            arr[k] = left_arr[i]    #Then, the index i is incremented to move to the next element in left_arr
            i += 1
        else:
            arr[k] = right_arr[j]   #If not left array then the current element of right_arr is placed in the original array at index k
            j += 1     # and the index j is incremented to move to the next element in right_arr
        k += 1
    
    while i < len(left_arr):   #If there are any remaining elements in left_arr, they are copied to the original array
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):   #If there are any remaining elements in right_arr, they are copied to the original array
        arr[k] = right_arr[j]
        j += 1
        k += 1

def main():
    try:
        arr = []
        n = input("Enter the elements separated by spaces: ")
        elements = n.split()
        
        for i in elements:
            if i.isdigit():   #to check if the input is a digit or not
                arr.append(int(i))   #to convert the input to an integer and append it to the array
            else:   
                raise ValueError   #to raise a ValueError if the input is not a digit
    
    except ValueError:      #Defining the exception handling for ValueError
        print("Enter all Integers value only") 
        return

    print("Choose the sorting technique:")
    print("1. Quick Sort")
    print("2. Merge Sort")
    print("3. Bubble Sort")
        
    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice == 1:
        sorted_arr = quick_sort(arr)
        print("Sorted array using Quick Sort:", [int(x) for x in sorted_arr])  #not required to convert to int as quick_sort already returns a list of integers
    elif choice == 2:
        merge_sort(arr, 0, len(arr) - 1)
        print("Sorted array using Merge Sort:", arr)
    elif choice == 3:
        sorted_arr = bubble_sort(arr)
        print("Sorted array using Bubble Sort:", sorted_arr)
    else:
        print("Invalid choice. Please choose either 1, 2, or 3.")
    
if __name__ == "__main__":
    main()
