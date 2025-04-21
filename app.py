from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is Efimka AI Assistant!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    message = data.get('message', '')
    response = f"Efimka received: {message}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
