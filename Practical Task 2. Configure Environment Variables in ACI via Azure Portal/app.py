import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greeting = os.getenv('GREETING', 'Hello, World!')
    return greeting

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
