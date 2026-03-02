from flask import Flask, jsonify
app = Flask(__name__)
tasks = []

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'flaskops'})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks, 'count': len(tasks)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
