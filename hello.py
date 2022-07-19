from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Team! Smart mobility FCSD  good afternoon07/19'

if __name__ == '__main__':
    app.run(debug=True)
