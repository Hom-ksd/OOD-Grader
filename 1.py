def find_min_x(arr, k):
    def can_partition(x):
        partitions = 0
        current_sum = 0

        for num in arr:
            current_sum += num
            if current_sum > x:
                partitions += 1
                current_sum = num

        return partitions + 1 <= k

    left, right = max(arr), sum(arr)

    while left < right:
        mid = (left + right) // 2
        if can_partition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# ตัวอย่างการใช้งาน
arr = [1, 2, 3, 4, 5,]
k = 1
min_x = find_min_x(arr, k)
print("k :", k, "x :", min_x)
