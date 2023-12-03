def BubbleSort (numbers):
    states = []

    # Iteramos sobre la lista de números, desde el principio hasta el final.
    for i in range(len(numbers) - 1):
        # Para cada iteración, comparamos los dos elementos más cercanos de la lista.
        for j in range(len(numbers) - i - 1):
            # Si el primer elemento es mayor que el segundo, los intercambiamos.
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        # Añadimos el estado actual de la lista de números a la lista de estados.
        states.append(numbers.copy())

    return states


def InsertionSort (numbers):
    pass

def MergeSort (numbers):
    pass

def HeapSort (numbers):
    pass

def QuickSort (numbers):
    pass

def CountingSort (numbers):
    pass

def RadixSort (numbers):
    pass

def BucketSort (numbers):
    pass