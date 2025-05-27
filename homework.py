nums = [5 ,7 ,10 ,26]
if len(nums) > 1:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)
