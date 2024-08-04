from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_array', methods=['GET'])
def generate_array():
    array = [random.randint(1, 100) for _ in range(50)]
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

@app.route('/binary_sort', methods=['POST'])
def binary_sort(): 
    array = request.json['array']
    steps = []
    for i in range(1, len(array)):
        left = 0 
        right = len(array) - 1
        while left <= right: 
            mid = (left + right) // 2
            if array[mid] < array[i]:
                left = mid + 1
            else:
                right = mid - 1
        array.insert(left, array.pop(i))
        steps.append(array[:])
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
