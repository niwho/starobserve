# _*_coding:utf-8_*_
from . import hello
from flask import request, session
import time


@hello.route('/')
def index():
    delay = float(request.args.get('delay') or 1)
    #resp = requests.get(f'{api_url}?delay={delay}')
    print("###########", session.get("test"))
    print(request.cookies.get("session"))
    session["test"] = time.time()
    return 'app:Hello World! ' #+ resp.text