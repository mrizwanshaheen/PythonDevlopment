let currentPin = '';

function appendPin(num) {
    if (currentPin.length < 4) {
        currentPin += num;
        updatePinDisplay();
    }
}

function clearPin() {
    currentPin = '';
    updatePinDisplay();
}

function updatePinDisplay() {
    const display = document.getElementById('pin-display');
    display.innerText = '*'.repeat(currentPin.length).padEnd(4, '-');
}

async function submitPin() {
    if (currentPin.length !== 4) return;

    const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pin: currentPin })
    });

    const data = await response.json();
    if (data.success) {
        window.location.href = '/withdraw';
    } else {
        showMessage(data.message, true);
        currentPin = '';
        updatePinDisplay();
    }
}

async function submitRegistration() {
    if (currentPin.length !== 4) return;

    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pin: currentPin })
    });

    const data = await response.json();
    if (data.success) {
        showMessage("PIN Set Successfully!", false);
        setTimeout(() => {
            window.location.href = '/login';
        }, 1000);
    } else {
        showMessage(data.message, true);
        currentPin = '';
        updatePinDisplay();
    }
}

function showMessage(text, isError) {
    const msg = document.getElementById('message');
    msg.innerText = text;
    msg.style.color = isError ? '#e74c3c' : '#2ecc71';
}

async function resetPin() {
    if (!confirm('Are you sure you want to reset your PIN? This will clear your account data.')) return;

    const response = await fetch('/reset', {
        method: 'POST'
    });

    const data = await response.json();
    if (data.success) {
        window.location.href = '/register';
    }
}

// Withdrawal Logic
let withdrawalAmount = 0;

function setAmount(amount) {
    withdrawalAmount = amount;
    document.getElementById('custom-amount').value = amount;
}

async function submitWithdraw() {
    const customInput = document.getElementById('custom-amount');
    if (customInput && customInput.value) {
        withdrawalAmount = parseInt(customInput.value);
    }

    if (!withdrawalAmount || withdrawalAmount <= 0) return;

    const response = await fetch('/withdraw', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: withdrawalAmount })
    });

    const data = await response.json();
    if (data.success) {
        document.getElementById('balance').innerText = data.new_balance;
        showModal();
    } else {
        alert(data.message);
    }
}

function showModal() {
    document.getElementById('successModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('successModal').style.display = 'none';
    withdrawalAmount = 0;
    document.getElementById('custom-amount').value = '';
}

function logout() {
    window.location.href = '/logout';
}
