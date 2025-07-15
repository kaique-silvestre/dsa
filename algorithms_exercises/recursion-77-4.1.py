# Algorithms 
# Page 77 
# Ex 4.1
# Some todos os números dentro de um array e retorno valor total usando recursão
# using recursion sum every number inside an array 

"""
Resolution algorithm
1. Create the function
2. If len(array) == 0 then we return 0
3. else we sum the last element with the all the others elements  
4. Do it again! using the function in the recreated list without the last element  
"""


# First try, I know it modifies the original arr. I would include a line that copies the original array if I havent found a better solution
def recursive_sum(arr):
  if len(arr) == 0:
    return 0
  var = arr.pop()
  somatotal = var + recursive_sum(arr)
  return somatotal



def recursive_sum01(arr):
  if len(arr) == 0:
    return 0
  return arr[-1] + recursive_sum01(arr[:-1]) # arr[-1]-> Selects the last element; arr[:-1] creates a new list without the last element


# Simplefy the code
def recursive_sum02(arr):
  return 0 if len(arr) == 0 else arr[-1] + recursive_sum02(arr[:-1])