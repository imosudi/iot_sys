from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


from . import routes