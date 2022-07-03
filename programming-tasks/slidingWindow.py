def max_sum(nums, k):
  max_sum = 0
  for i in range(len(nums)-k+1):
    cur_sum = 0
  for j in range(0, k):
    cur_sum += nums[i+j]
  max_sum = max(max_sum, cur_sum)
  return max_sum

print(max_sum([100,200,300,400],2))
