import random
import time
import sys
sys.setrecursionlimit(5000)

def quicksort_pivo_aleatorio(lista):
    if len(lista) < 2:
        return lista
    pivo = random.choice(lista)  
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort_pivo_aleatorio(esquerda) + meio + quicksort_pivo_aleatorio(direita)

def quicksort_pivo_fixo(lista):
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort_pivo_fixo(esquerda) + meio + quicksort_pivo_fixo(direita)

def tempo(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    sort_function(arr_copy)
    return (time.time() - start_time) * 1000  # Tempo em ms

lista_tamanhos = [10000, 20000, 30000]

for tamanho in lista_tamanhos:
    print(f"\nTeste com {tamanho} elementos:")
    
    # Melhor caso (dados aleatórios)
    lista_aleatoria = list(range(tamanho))
    random.shuffle(lista_aleatoria)
    melhor_caso_pivo_aleatorio = tempo(quicksort_pivo_aleatorio, lista_aleatoria)
    melhor_caso_pivo_fixo = tempo(quicksort_pivo_fixo, lista_aleatoria)
    
    # Pior caso (dados quase ordenados (raro) )
    lista_quase_ordenada = list(range(tamanho))
    swap_count = int(tamanho * 0.05)
    for _ in range(swap_count):
        i, j = random.sample(range(tamanho), 2)
        lista_quase_ordenada[i], lista_quase_ordenada[j] = lista_quase_ordenada[j], lista_quase_ordenada[i]
    pior_caso_pivo_aleatorio = tempo(quicksort_pivo_aleatorio, lista_quase_ordenada)
    pior_caso_pivo_fixo = tempo(quicksort_pivo_fixo, lista_quase_ordenada)
    
    # Exibir resultados
    print(f"\nMelhor caso (dados aleatórios)")
    print(f"Quicksort (pivô aleatorio): {melhor_caso_pivo_aleatorio:.2f} ms")
    print(f"Quicksort (pivô fixo): {melhor_caso_pivo_fixo:.2f} ms")
    
    print(f"\nPior caso (dados quase ordenados)")
    print(f"Quicksort (pivô aleatorio): {pior_caso_pivo_aleatorio:.2f} ms")
    print(f"Quicksort (pivô fixo): {pior_caso_pivo_fixo:.2f} ms")

