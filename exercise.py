candidates = [2, 5, 2, 1, 2]
target = 5
def backtrack(start, path, target):
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        backtrack(i + 1, path + [candidates[i]], target - candidates[i])
candidates.sort()
result = []
backtrack(0, [], target)
print(result)



