# -*-coding:utf-8 -*-
from flask import g, make_response, jsonify
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from threading import Thread
from .. import app, mail
from ..models import Tokenused

auth = HTTPTokenAuth(scheme='Xls')
serializer = Serializer(app.config['SECRET_KEY'])

@auth.verify_token
def verify_token(token):
    g.username = None
    try:
        data = serializer.loads(token)
        g.token = token
    except:
        return False
    if 'username' in data:
        g.username = data['username']
        return True
    return False

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'token error'}), 401)

def get_toekn(username,time):
    s = Serializer(app.config['SECRET_KEY'], expires_in=time)
    return s.dumps({'username': username}).decode('utf-8')

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(msg):
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

def token_used(token):
    if Tokenused.query.filter_by(token=token).first():
        return True
    else:
        Tokenused(token=token).save()
        return False