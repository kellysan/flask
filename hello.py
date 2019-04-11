#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       hello
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-10
#    Change Activity:  2019-04-10:

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'
gitg

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)