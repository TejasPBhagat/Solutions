
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        if target == nums[i] + nums[i+1]:
            x = sum(nums)
            print(i,i+1)


# Runtime : 57ms          

twoSum([1,2,3,4,5,6], 9)