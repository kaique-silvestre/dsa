# That's my first try of doing a binary search... god knows how long i take 
# but it is wrong, i am comparing the values not the index...

def pesquisa_binaria(lista, item):
    cont = 0
    menor = 0
    maior = len(lista) - 1
    while True:
        cont += 1
        metade = (menor + maior) // 2 
        if metade < item: 
            menor = metade 
        if metade > item: 
            maior = metade 
        if metade == item: 
            return metade
        if item not in lista:
            return -1


lista = range(101)
print(pesquisa_binaria(lista, 57))
