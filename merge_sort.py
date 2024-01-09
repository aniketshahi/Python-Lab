def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Get user input for the list of numbers
try:
    input_str = input("Enter a list of numbers separated by space: ")
    num_list = list(map(int, input_str.split()))
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

# Display the original list
print("Original List:", num_list)

# Perform merge sort on the list
merge_sort(num_list)

# Display the sorted list
print("Sorted List:", num_list)
