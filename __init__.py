from flask import Flask,session,redirect, render_template, request
from algoritmos import *
import random
import time

app=Flask(__name__,static_folder='static',template_folder='templates')
app.secret_key = 'SortApp_Algoritmos_Level1'  # Clave secreta para la sesión de Flask


@app.route("/")
def index():
    return render_template('index.html')

@app.post("/ordenar")
def ordenar():
    data=request.get_json()
    numbers=[eval(num) for num in data.get('numbers')] if not data['randomState'] else [random.randint(0,1000) for number in range(random.randint(10,30))]
    ti=time.time()
    if data.get('algoritmo')=='Bubble':results=BubbleSort(numbers)
    if data.get('algoritmo')=='Insertion':results=InsertionSort(numbers)
    if data.get('algoritmo')=='Merge':results=MergeSort(numbers)
    if data.get('algoritmo')=='Heap':results=HeapSort(numbers)
    if data.get('algoritmo')=='Quick':results=QuickSort(numbers)
    if data.get('algoritmo')=='Counting':results=CountingSort(numbers)
    if data.get('algoritmo')=='Radix':results=RadixSort(numbers)
    if data.get('algoritmo')=='Bucket':results=BucketSort(numbers)
    tiempo=time.time()-ti
    print(results)
    return {'code':300,'states':results,'time_elapsed':tiempo}

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')