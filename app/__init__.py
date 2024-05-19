import logging
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

from . import routes