from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dirisala! last trail success 07/14'

if __name__ == '__main__':
    app.run(debug=True)
