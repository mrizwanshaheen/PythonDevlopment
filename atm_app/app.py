from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DATA_FILE = 'user_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return None

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    user = load_data()
    if not user:
        return redirect(url_for('register'))
    if 'logged_in' in session:
        return redirect(url_for('withdraw'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    user = load_data()
    if user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = request.get_json()
        pin = data.get('pin')
        if not pin or len(pin) != 4:
            return jsonify({'success': False, 'message': 'PIN must be 4 digits'})
        
        user_data = {
            'pin': pin,
            'balance': 5000  # Default starting balance
        }
        save_data(user_data)
        return jsonify({'success': True})
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = load_data()
    if not user:
        return redirect(url_for('register'))

    if request.method == 'POST':
        data = request.get_json()
        pin = data.get('pin')
        if pin == user['pin']:
            session['logged_in'] = True
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Invalid PIN'})
    return render_template('login.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    user = load_data()
    
    if request.method == 'POST':
        data = request.get_json()
        amount = int(data.get('amount'))
        
        if amount > user['balance']:
            return jsonify({'success': False, 'message': 'Insufficient Funds'})
        
        user['balance'] -= amount
        save_data(user)
        return jsonify({'success': True, 'new_balance': user['balance']})
        
    return render_template('withdraw.html', balance=user['balance'])

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('thankyou'))

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/reset', methods=['POST'])
def reset():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    session.pop('logged_in', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
