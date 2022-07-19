from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Team! Smart mobility FCSD 07/19'

if __name__ == '__main__':
    app.run(debug=True)
