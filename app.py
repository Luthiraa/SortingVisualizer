from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_array', methods=['GET'])
def generate_array():
    array = [random.randint(1, 100) for _ in range(100)]
    return jsonify(array)

@app.route('/bubble_sort', methods=['POST'])
def bubble_sort():
    array = request.json['array']
    steps = []
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                steps.append(array[:])
    return jsonify(steps)

@app.route('/insertion_sort', methods=['POST'])
def insertion_sort():
    array = request.json['array']
    steps = []
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        steps.append(array[:])  
    return jsonify(steps)

@app.route('/selection_sort', methods=['POST'])
def selection_sort(): 
    array = request.json['array']
    steps = []
    for i in range(len(array)-1): 
        currMin = i
        for j in range(i+1, len(array)): 
            if array[j] < array[currMin]: 
                currMin = j
        
        array[i], array[currMin] = array[currMin],array[i]
        steps.append(array[:])
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)