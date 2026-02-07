let currentInput = '0';
let previousInput = '';
let operator = null;
let history = '';

const displayElement = document.getElementById('display');
const historyElement = document.getElementById('history');

function updateDisplay() {
    displayElement.innerText = currentInput;
    historyElement.innerText = history;
}

function appendNumber(number) {
    if (currentInput === '0' && number !== '.') {
        currentInput = number;
    } else {
        if (number === '.' && currentInput.includes('.')) return;
        currentInput += number;
    }
    updateDisplay();
}

async function appendOperator(op) {
    if (currentInput === '' && previousInput === '') return;

    // If user changes operator without entering new number
    if (currentInput === '' && previousInput !== '') {
        operator = op;
        history = `${previousInput} ${op}`;
        updateDisplay();
        return;
    }

    if (previousInput !== '') {
        await calculate(true); // invalidating the previous operator/input by calculating
    }

    operator = op;
    previousInput = currentInput;
    history = `${previousInput} ${op}`;
    currentInput = '';
    updateDisplay();
}


function clearDisplay() {
    currentInput = '0';
    previousInput = '';
    operator = null;
    history = '';
    updateDisplay();
}

function deleteLast() {
    if (currentInput.length === 1) {
        currentInput = '0';
    } else {
        currentInput = currentInput.slice(0, -1);
    }
    updateDisplay();
}

async function calculate(isChained = false) {
    if (previousInput === '' || currentInput === '') return;

    let expression = `${previousInput}${operator}${currentInput}`;

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression }),
        });

        const data = await response.json();

        if (response.ok) {
            currentInput = data.result.toString();
            if (!isChained) {
                // If this was a manual =, clear the operator state 
                // but keep result in currentInput for next op
                history = `${expression} =`;
                previousInput = '';
                operator = null;
            } else {
                // If chained (e.g. 1+2+), we just updated currentInput to 3
                // appendOperator will then move it to previousInput
            }
        } else {
            currentInput = 'Error';
            console.error(data.error);
        }
    } catch (error) {
        currentInput = 'Error';
        console.error('Error:', error);
    }
    if (!isChained) {
        updateDisplay();
    }
}
