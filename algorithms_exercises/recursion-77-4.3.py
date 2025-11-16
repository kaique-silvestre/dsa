# Algorithms 
# Page 77 
# Ex 4.3
# Encontre o valor mais alto em uma list
# Find the highest value inside a lista


var = [1, 2, 3, 4, 5]


# Retornar o maior valor de uma lista
# Percorrer valor por valor 
# o primeiro valor é o maior valor que conhecemos
# Comparar primerio valor com os valores seguintes?????
# Caso base é quando não há comprações pra serem feitas

# Caso-base: Se 

# This is my first exercise version, i know we are calling the function twice, this is a problem!
def recursion_highest_value00(arr):
  try: 
    if len(arr) == 1:
      return arr[-1]
    return arr[-1] if arr[-1] >= recursion_highest_value00(arr[:-1]) else recursion_highest_value00(arr[:-1])
  except IndexError:
    return None

# This fixes the problem of calling the func twice
def recursion_highest_value01(arr):
  try: 
    if len(arr) == 1:
      return arr[-1]
    func = recursion_highest_value01(arr[:-1])
    return arr[-1] if arr[-1] >= func else func
  except IndexError:
    return None

# Chatgpt argues that is better use a conditional if, instead of a try-except block 'cause it is more explicit than try-except
def recursion_highest_value02(arr):
    if arr == []:
      return None
    if len(arr) == 1:
      return arr[-1]
    func = recursion_highest_value02(arr[:-1])
    return arr[-1] if arr[-1] >= func else func





arr = []
print()
print(recursion_highest_value02(arr))