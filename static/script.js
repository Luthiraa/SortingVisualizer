const arrayContainer = document.getElementById('array-container');
let originalArray = [];

async function generateArray() {
    const response = await fetch('/generate_array');
    originalArray = await response.json();
    renderArray(originalArray);
}

async function bubbleSort() {
    const array = [...originalArray]; // Create a copy of the original array

    const response = await fetch('/bubble_sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ array })
    });

    const steps = await response.json();
    for (let step of steps) {
        await renderArray(step);
        await sleep(5);
    }
}

async function insertionSort() {
    const array = [...originalArray]; // Create a copy of the original array

    const response = await fetch('/insertion_sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ array })
    });

    const steps = await response.json();
    for (let step of steps) {
        await renderArray(step);
        await sleep(10);
    }
}

async function selectionSort() {
    const array = [...originalArray]; // Create a copy of the original array

    const response = await fetch('/selection_sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ array })
    });

    const steps = await response.json();
    for (let step of steps) {
        await renderArray(step);
        await sleep(10);
    }
}
function renderArray(array) {
    arrayContainer.innerHTML = '';
    const containerWidth = arrayContainer.clientWidth;
    const barWidth = containerWidth / array.length - 2; // Subtracting 2 for the margin
    array.forEach(value => {
        const bar = document.createElement('div');
        bar.className = 'bar';
        bar.style.height = `${value * 4}px`;
        bar.style.width = `${barWidth}px`;
        arrayContainer.appendChild(bar);
    });
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

generateArray();