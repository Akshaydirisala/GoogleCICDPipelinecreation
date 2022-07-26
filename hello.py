from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'SMART MOBILITY Team 07/26 good afternoon 12:35'

if __name__ == '__main__':
    app.run(debug=True)
