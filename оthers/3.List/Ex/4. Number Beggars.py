nums_str = input().split(", ")
count = int(input())
nums = [int(num) for num in nums_str]

result = [0] * count
for i in range(len(nums)):
    index = i % count
    result[index] += nums[i]

print(result)
