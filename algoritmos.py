import math

def BubbleSort (numbers):
    states = []

    # Iteramos sobre la numbers de números, desde el principio hasta el final.
    for i in range(len(numbers) - 1):
        # Para cada iteración, comparamos los dos elementos más cercanos de la numbers.
        for j in range(len(numbers) - i - 1):
            # Si el primer elemento es mayor que el segundo, los intercambiamos.
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

                # Añadimos el estado actual de la numbers de números a la numbers de estados.
                states.append(numbers.copy())

    return states


def InsertionSort (numbers):
    states=[]
    for i in range(1, len(numbers)):
        valor_actual = numbers[i]
        posicion = i
        
        while posicion > 0 and numbers[posicion - 1] > valor_actual:
            numbers[posicion] = numbers[posicion - 1]
            posicion -= 1
            states.append(numbers.copy())

        
        numbers[posicion] = valor_actual
        states.append(numbers.copy())
    
    return states



def MergeSort(numbers, states=None):
    if states is None:
        states = []

    def _merge_sort(numbers):
        if len(numbers) > 1:
            mid = len(numbers) // 2
            L = numbers[:mid]
            R = numbers[mid:]
            _merge_sort(L)
            _merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    numbers[k] = L[i]
                    i += 1
                else:
                    numbers[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                numbers[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                numbers[k] = R[j]
                j += 1
                k += 1
            states.append(numbers.copy())

    _merge_sort(numbers)
    return states

def HeapSort(arr):
    states=[]
    def heapify(arr, n, i):
        largest = i 
        l = 2 * i + 1 
        r = 2 * i + 2 
    
        if l < n and arr[i] < arr[l]:
            largest = l
    
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i]) 
    
            heapify(arr, n, largest)
            states.append(arr.copy())

    n = len(arr)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)
    return states

def QuickSort(array, states=None):
    if states is None:
        states = []
    def partition(array, low, high):  
        # Pivote el de la derecha
        pivot = array[high]

        # Apuntador del último elemento más pequeño
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
            # Avanzar apuntador
                i = i + 1
                # Intercambiar elementos
                (array[i], array[j]) = (array[j], array[i])

        # Al final intercambiar el pivote
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        states.append(array.copy())
        # Regresa la posición final del pivote
        return i + 1
    
    def _quicksort(array, low, high):
        if low < high:
            # Dividir y acomodar pivote
            pi = partition(array, low, high)
        
            _quicksort(array, low, pi - 1)
            _quicksort(array, pi + 1, high)
    
    _quicksort(array,0,len(array)-1)

    return states

def CountingSort (numbers):
    states=[numbers]
     # Encuentra el valor máximo en el arreglo
    max_value = max(numbers)
    
    # Crea un arreglo de conteo para contar las ocurrencias de cada elemento
    count = [0] * (max_value + 1)
    
    # Llena el arreglo de conteo
    for num in numbers:
        count[num] += 1
    
    # Reconstruye el arreglo ordenado
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])
        states.append(sorted_arr.copy())

    lista_sin_duplicados = []
    for elemento in states:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)

    
    return lista_sin_duplicados

def RadixSort (numbers):
    states=[numbers.copy()]
    def countingSort(arr, exp1):
 
        n = len(arr)
    
        # The output array elements that will have sorted arr
        output = [0] * (n)
    
        # initialize count array as 0
        count = [0] * (10)
    
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]
    
        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        return output

    max1 = max(numbers)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        numbers=countingSort(numbers, exp)
        states.append(numbers.copy())
        exp *= 10
    
    return states


def BucketSort (x):
    states=[x.copy()]
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
 
    # Put array elements in different buckets
    for j in x:
        index_b = math.floor(slot_num*j/max(x)) if j!=max(x) else 9
        arr[index_b].append(j)
 
    # Sort individual buckets
    for i in range(slot_num):
        states.append(arr[i].copy())
        sorted_bucket=InsertionSort(arr[i])
        if len(sorted_bucket)>0:states=[*states,*sorted_bucket.copy()]
        arr[i] = sorted_bucket[-1] if len(sorted_bucket)>0 else []
 
    # concatenate the result
    k = 0
    result=[]
    states.append(x.copy())
    for i in range(slot_num):
        result=[*result,*arr[i]]
        states.append(result.copy())

    return states