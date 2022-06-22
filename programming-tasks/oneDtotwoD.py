original = [1,2,3]
m = 1
n = 3

def construct2DArray(original, m: int, n: int):
  idx = 0
  if len(original) == (m*n):
      new_arr = []
      for i in range(m):
        temp = []
        for j in range(n):
          temp.append(original[idx])
          idx += 1
        new_arr.append(temp)
      return new_arr
  return []

print(construct2DArray(original, m, n))

              
  