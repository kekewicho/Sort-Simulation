from flask import Flask,session,redirect, render_template, request
from algoritmos import *

app=Flask(__name__,static_folder='static',template_folder='templates')
app.secret_key = 'SortApp_Algoritmos_Level1'  # Clave secreta para la sesión de Flask


@app.route("/")
def index():
    return render_template('index.html')

@app.post("/ordenar")
def ordenar():
    data=request.get_json()
    numbers=[eval(num) for num in data.get('numbers')]
    if data.get('algoritmo')=='Bubble':results=BubbleSort(numbers)
    if data.get('algoritmo')=='Insertion':pass
    if data.get('algoritmo')=='Merge':pass
    if data.get('algoritmo')=='Heap':pass
    if data.get('algoritmo')=='Quick':pass
    if data.get('algoritmo')=='Counting':pass
    if data.get('algoritmo')=='Radix':pass
    if data.get('algoritmo')=='Bucket':pass
    print(results)
    return {'code':300,'states':results}

if __name__=='__main__':
    app.run(debug=True)