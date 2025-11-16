# Algorithms 
# Page 77 
# Ex 4.4

def binary_search(arr, target):
  low = 0
  high = len(arr) -1

  while high >= low:
    mid = (low + high) // 2

    if arr[mid] > target:
      high = mid - 1
    elif arr[mid] < target:
      low = mid + 1
    else:
      return mid
  return None


# First Try -- it's wrong:
def recursive_binary_search00(arr, target):
  mid = len(arr) // 2
  if arr[mid] == target:
    return mid
  if arr[mid] > target:
    return recursive_binary_search00(arr[:mid], target)
  if arr[mid] < target:
    return recursive_binary_search00(arr[mid+1:], target)
  return None

"""
# Eu entendi em parte o problema do meu algoritmo:
se o target for menor que o mid do array o index do array continua preservado 
mesmo que a lista seja recriada:

[10, 20, 30, / 40, 50, 60]
  0   1   2     3   4   5 

Porém se o target for maior que o mid, meu algoritmo irá recriar o array e por obvio haverá novos indexes:

40, 50, 60]
  0   1   2

"""

# terrible algorithm
def recursive_binary_search01(arr, target):
  if len(arr) == 0:
    return None
  mid = len(arr) // 2
  if arr[mid] == target:
    return mid
  if arr[mid] > target:
    return recursive_binary_search01(arr[:mid], target)  
  result = recursive_binary_search01(arr[mid+1:], target)
  if result is not None:
    return mid + 1 + result
  else:
    return None 
  
  
# Finally
def recursive_binary_search(arr, target = 0, start = 0, end = None):
  if end is None:
    end = len(arr) - 1
  if start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      return recursive_binary_search(arr, target, start, mid - 1)
    else:
      return recursive_binary_search(arr, target, mid + 1, end)
  return None

var = []
var01 = [20, 40, 60, 70, 100]
print(recursive_binary_search(var01, 100))
print(recursive_binary_search(var01, 20))
print(recursive_binary_search(var01, 50))
print(recursive_binary_search(var, 100))