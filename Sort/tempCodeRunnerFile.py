def heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def display_heap(arr, i, n):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    print(f"Parent: {arr[i]}", end="")
    if left_child < n:
        print(f"   Left Child: {arr[left_child]}", end="")
    if right_child < n:
        print(f"   Right Child: {arr[right_child]}", end="")
    print()

input_str = input("Enter a list of numbers separated by commas: ")
input_list = [int(x) for x in input_str.split(",")]

# Build a min heap from the input list
build_min_heap(input_list)

print("Heap:")
for i in range(len(input_list)):
    display_heap(input_list, i, len(input_list))


print(input_list)