#coding:utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello WSGI'

if __name__ == '__main__':
    app.run()
