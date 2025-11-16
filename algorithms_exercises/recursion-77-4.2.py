# Algorithms 
# Page 77 
# Ex 4.2
# Escreva uma função recursiva que conte a quantidade de elementos em uma lista 
# Write a function that counts how many elements there are inside a list

def recursive_count(arr: list, count=0):
  if len(arr) == 0:
    return count
  return recursive_count(arr[:-1], count+1)


print(recursive_count([10,10,10,10]))



def recursive_count01(arr):
  if arr == []:
    return 0
  return 1 + recursive_count01(arr[:-1]) # I was having a hard time trying to understand what this means 
# I understood, It is like: 1 + (1 + (1 + (0)))

                      #   1 + (1 + (1 + (0)))
print(recursive_count01([100, 100, 100]))