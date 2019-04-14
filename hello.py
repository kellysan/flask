#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       hello
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-10
#    Change Activity:  2019-04-10:

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


#  路由  静态文件
@app.route('/')
def hello_world():
    # return 'hello world!'
    return  render_template("index.html")



# 变量规则

@app.route('/add/<name>')
def add(name):
    return 'My name is %s' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return "blog id is %d" % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return "Revision Number %f" % revNo

# url构建
@app.route('/admin')
def hello_admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s as Guest" % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return  redirect(url_for('hello_guest', guest=name))



# 配合表单提交 HTTP 方法

@app.route('/success/<name>')
def success(name):
    return '%s success' % name


@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for('success', name= user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name= user))


# jinja模板
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


# 在模板中使用条件判断
@app.route('/hello1/<int:score>')
def hello_for(score):
    return render_template('hello1.html', marks = score)


# 在模板中使用循环语句
@app.route('/result/')
def result():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('hello2.html', result = dict)

# Request对象
"""
Form - 它是一个字典对象，包含表单参数及其值的键和值对。
args - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。
Cookies  - 保存Cookie名称和值的字典对象。
files - 与上传文件有关的数据。
method - 当前请求方法。
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)