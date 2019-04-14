#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       main
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-12
#    Change Activity:  2019-04-12:

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return  render_template('result.html', result = result)


if __name__ == '__main__':
    app.run(debug=True)