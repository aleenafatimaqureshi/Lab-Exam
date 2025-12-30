from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins Pipeline!"

if __name__ == '__main__':
    # Listens on all interfaces so Jenkins can run it if needed
    app.run(host='0.0.0.0', port=5000)from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins Pipeline!"

if __name__ == '__main__':
    # Listens on all interfaces so Jenkins can run it if needed
    app.run(host='0.0.0.0', port=5000)
