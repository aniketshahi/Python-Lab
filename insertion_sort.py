def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Get user input for the list of numbers
try:
    input_str = input("Enter a list of numbers separated by space: ")
    num_list = list(map(int, input_str.split()))
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

# Display the original list
print("Original List:", num_list)

# Perform insertion sort on the list
insertion_sort(num_list)

# Display the sorted list
print("Sorted List:", num_list)
