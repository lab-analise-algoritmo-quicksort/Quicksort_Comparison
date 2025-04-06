import random
import time
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(100000)

trocas_fixo = 0
trocas_med3 = 0

def quicksort_fixo(arr):
    global trocas_fixo
    def _quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quicksort(arr, low, pivot_index - 1)
            _quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        global trocas_fixo
        pivot = arr[low]
        left = low + 1
        right = high
        while True:
            while left <= right and arr[left] <= pivot:
                trocas_fixo += 1
                left += 1
            while left <= right and arr[right] > pivot:
                trocas_fixo += 1
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right

    _quicksort(arr, 0, len(arr) - 1)

def quicksort_mediana3(arr):
    global trocas_med3
    if len(arr) <= 1:
        return arr
    primeiro = arr[0]
    meio = arr[len(arr)//2]
    ultimo = arr[-1]
    pivot = sorted([primeiro, meio, ultimo])[1]
    menores, iguais, maiores = [], [], []
    for x in arr:
        trocas_med3 += 1
        if x < pivot:
            menores.append(x)
        elif x == pivot:
            iguais.append(x)
        else:
            maiores.append(x)
    return quicksort_mediana3(menores) + iguais + quicksort_mediana3(maiores)

def gerar_lista_aleatoria(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]

def gerar_lista_50_ordenada(tamanho):
    metade = tamanho // 2
    primeira = sorted([random.randint(1, 100000) for _ in range(metade)])
    segunda = [random.randint(1, 100000) for _ in range(tamanho - metade)]
    return primeira + segunda


tamanho_lista = 50000
passos = [10, 20, 30, 40, 50]

tempos_fixo = []
tempos_med3 = []
trocas_fixo_lista = []
trocas_med3_lista = []

tempos_fixo_50 = []
tempos_med3_50 = []
trocas_fixo_50_lista = []
trocas_med3_50_lista = []

# Lista Aleatoria
for num_testes in passos:
    tempo_total_fixo = 0
    tempo_total_med3 = 0
    trocas_total_fixo = 0
    trocas_total_med3 = 0

    for _ in range(num_testes):
        lista = gerar_lista_aleatoria(tamanho_lista)
        copia = lista[:]
        trocas_fixo = 0
        inicio = time.time()
        quicksort_fixo(copia)
        tempo_total_fixo += time.time() - inicio
        trocas_total_fixo += trocas_fixo

        copia = lista[:]
        trocas_med3 = 0
        inicio = time.time()
        quicksort_mediana3(copia)
        tempo_total_med3 += time.time() - inicio
        trocas_total_med3 += trocas_med3

    tempos_fixo.append(tempo_total_fixo)
    tempos_med3.append(tempo_total_med3)
    trocas_fixo_lista.append(trocas_total_fixo)
    trocas_med3_lista.append(trocas_total_med3)

# 50% arrumado
for num_testes in passos:
    tempo_total_fixo = 0
    tempo_total_med3 = 0
    trocas_total_fixo = 0
    trocas_total_med3 = 0

    for _ in range(num_testes):
        lista = gerar_lista_50_ordenada(tamanho_lista)
        copia = lista[:]
        trocas_fixo = 0
        inicio = time.time()
        quicksort_fixo(copia)

        tempo_total_fixo += time.time() - inicio
        trocas_total_fixo += trocas_fixo
        copia = lista[:]
        trocas_med3 = 0
        inicio = time.time()
        quicksort_mediana3(copia)

        tempo_total_med3 += time.time() - inicio
        trocas_total_med3 += trocas_med3

    tempos_fixo_50.append(tempo_total_fixo)
    tempos_med3_50.append(tempo_total_med3)

    trocas_fixo_50_lista.append(trocas_total_fixo)
    trocas_med3_50_lista.append(trocas_total_med3)

# Tempo de lista aleatória
plt.figure(figsize=(10, 5))
plt.plot(passos, tempos_fixo, label='Pivô Fixo', marker='o')
plt.plot(passos, tempos_med3, label='Mediana de 3', marker='o')
plt.xlabel('Quantidade de listas ordenadas')
plt.ylabel('Tempo total (s)')
plt.title('Tempo - Lista Aleatória')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('tempo_lista_aleatoria.png')  # <- Salvar imagem
plt.show()

# Trocas de lista aleatória
plt.figure(figsize=(10, 5))
plt.plot(passos, trocas_fixo_lista, label='Pivô Fixo', marker='o')
plt.plot(passos, trocas_med3_lista, label='Mediana de 3', marker='o')
plt.xlabel('Quantidade de listas ordenadas')
plt.ylabel('Número total de trocas')
plt.title('Trocas - Lista Aleatória')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('trocas_lista_aleatoria.png')
plt.show()

# Tempo de Lista 50% 
plt.figure(figsize=(10, 5))
plt.plot(passos, tempos_fixo_50, label='Pivô Fixo', marker='o')
plt.plot(passos, tempos_med3_50, label='Mediana de 3', marker='o')
plt.xlabel('Quantidade de listas ordenadas')
plt.ylabel('Tempo total (s)')
plt.title('Tempo - Lista 50% Ordenada')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('tempo_lista_50_ordenada.png')
plt.show()

# Trocas de Lista 50%
plt.figure(figsize=(10, 5))
plt.plot(passos, trocas_fixo_50_lista, label='Pivô Fixo', marker='o')
plt.plot(passos, trocas_med3_50_lista, label='Mediana de 3', marker='o')
plt.xlabel('Quantidade de listas ordenadas')
plt.ylabel('Número total de trocas')
plt.title('Trocas - Lista 50% Ordenada')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('trocas_lista_50_ordenada.png')
plt.show()

