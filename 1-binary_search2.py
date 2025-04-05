# I have learned that the search should be performed by the array index instead of the value inside the index
# When using the len function to get the last value of an array, we subtract its value by one, because the array starts at zero, and the len function stars counting on one

def pesquisa_binaria(lista, item):
    cont = 0
    menor = 0
    maior = len(lista) - 1
    while menor <= maior:
        cont += 1
        metade = (menor + maior) // 2
        if lista[metade] == item:
            return f"O item está na posição: {metade}, foram feitas {cont} operações"
        if lista[metade] < item:
            menor = metade + 1 # We are adding plus one because we already know that the midpoint isn't in the right item, otherwise it would not pass the first "if"
        if lista[metade] > item:
            maior = metade - 1 # Same logic as before, we already know that the midpoint isn't the searched item, and how we know the number is lower than the midpoint we subtract one
    return None

lista = range(1000000000000)

print(pesquisa_binaria(lista, 1))        
