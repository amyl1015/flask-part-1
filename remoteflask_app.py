from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/Section')
def Section():
    return 'This is class 504'

@app.route('/Assignment')
def Assignment():
    return 'This is FLASK assignment'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

# This is bash code
# sudo nohup python3 remoteflask_app.py > log.txt 2>&1 &
