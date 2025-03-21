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

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break

def tempo(sort_function, arr, in_place=False):
    arr_copy = arr.copy()
    start_time = time.time()
    if in_place:
        sort_function(arr_copy)  # Algoritmos in-place
    else:
        sort_function(arr_copy)  # Algoritmos que retornam nova lista
    return (time.time() - start_time) * 1000  # Tempo em ms

lista_tamanhos = [10000]

for tamanho in lista_tamanhos:
    print(f"\nTeste com {tamanho} elementos:")
    
    #dados aleatórios
    lista_aleatoria = list(range(tamanho))
    random.shuffle(lista_aleatoria)
    melhor_caso_pivo_aleatorio = tempo(quicksort_pivo_aleatorio, lista_aleatoria)
    melhor_caso_pivo_fixo = tempo(quicksort_pivo_fixo, lista_aleatoria)
    melhor_caso_bubble = tempo(bubble_sort, lista_aleatoria, in_place=True)
    
    #dados quase ordenados
    lista_quase_ordenada = list(range(tamanho))
    swap_count = int(tamanho * 0.05)
    for _ in range(swap_count):
        i, j = random.sample(range(tamanho), 2)
        lista_quase_ordenada[i], lista_quase_ordenada[j] = lista_quase_ordenada[j], lista_quase_ordenada[i]
    pior_caso_pivo_aleatorio = tempo(quicksort_pivo_aleatorio, lista_quase_ordenada)
    pior_caso_pivo_fixo = tempo(quicksort_pivo_fixo, lista_quase_ordenada)
    pior_caso_bubble = tempo(bubble_sort, lista_quase_ordenada, in_place=True)
    
    # Exibir resultados
    print(f"\nDados aleatórios")
    print(f"QuickSort (pivô aleatório): {melhor_caso_pivo_aleatorio:.2f} ms")
    print(f"QuickSort (pivô fixo): {melhor_caso_pivo_fixo:.2f} ms")
    print(f"BubbleSort: {melhor_caso_bubble:.2f} ms")
    
    print(f"\nDados quase ordenados")
    print(f"QuickSort (pivô aleatório): {pior_caso_pivo_aleatorio:.2f} ms")
    print(f"QuickSort (pivô fixo): {pior_caso_pivo_fixo:.2f} ms")
    print(f"BubbleSort: {pior_caso_bubble:.2f} ms")

