def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Example usage
array = []
n = int(input("\n Enter number of elements to be Sort:"))
print("\n Enter the elements to be Sorted:")
for i in range(n):
    array.append(int(input()))

insertion_sort(array)

print("\nArray after Insertion sort:")
for i in range(n):
    print(f"a[{i}] = {array[i]}")
