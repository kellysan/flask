#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       cookie
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-14
#    Change Activity:  2019-04-14:

from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cookie.html')


@app.route('/setcookie', methods= ['POST', 'GET'])
def set_cookie():
    if request.method == 'POST':
        user = request.form['nm']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    return resp


@app.route('/getcookie')
def get_cookie():
   name = request.cookies.get('userID')
   return render_template('getkookie.html', result = name)


if __name__ == '__main__':
    app.run()