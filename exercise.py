nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
def quantity(nums):
    for i in nums:
        counter = nums.count(i)
        if counter >= 2:
            return True
        return False
print(quantity(nums))
