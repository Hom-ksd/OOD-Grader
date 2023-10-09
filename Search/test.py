def all_possible_splits(lst, n):
    if n == 1:
        return [[lst]]

    all_splits = []
    for i in range(1, len(lst) - n + 2):
        current = lst[:i]
        remaining_splits = all_possible_splits(lst[i:], n - 1)
        for split in remaining_splits:
            all_splits.append([current] + split)

    return all_splits

# Example usage:
Data,target = input("Enter Input : ").split("/")

Data = list(map(int,Data.split()))
target = int(target)

all_splits = all_possible_splits(Data, target)

mn = 1e9

for split in all_splits:
    # print(split)
    mx = 0
    for s in split:
        mx = max(mx,sum(s))
    mn = min(mx,mn)
print(mn)
