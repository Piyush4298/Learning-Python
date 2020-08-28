def sort(nums):
    for i in range(len(nums) - 1):
        min_pos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_pos]:
                min_pos = j

        nums[i], nums[min_pos] = nums[min_pos], nums[i]


nums = [5, 8, 3, 6, 2, 7]
sort(nums)
print(nums)
