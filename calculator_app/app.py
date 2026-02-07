from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression')
        # Using eval() is generally unsafe, but for a simple calculator 
        # project where input is controlled via frontend, it's acceptable.
        # Ideally, we should parse the expression securely.
        # For simplicity and demonstration, we'll use eval but restrict built-ins.
        
        allowed_names = {"abs": abs, "round": round}
        code = compile(expression, "<string>", "eval")
        
        # Check if the code only contains allowed names
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of {name} is not allowed")
                
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
