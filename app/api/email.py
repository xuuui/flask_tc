# -*-coding:utf-8 -*-
from flask import redirect, url_for
from flask_restful import Resource, request
from flask_mail import Message
from . import util
from .. import db, socketio
from ..models import User

class Email(Resource):
    def get(self, mailtoken, mail):
        if util.token_used(mailtoken):
            return redirect(url_for('main.mail', status=2))
        try:
            data = util.serializer.loads(mailtoken)
        except:
            return redirect(url_for('main.mail', status=0))
        if 'username' in data:
            username = data['username']
            u = User.query.filter_by(username=username).first()
            u.mail = mail
            u.activated = 1
            db.session.commit()
            socketio.emit('mailcheck', 1)
            return redirect(url_for('main.mail', status=1))
        return redirect(url_for('main.mail', status=0))

    @util.auth.login_required
    def post(self):
        root_url = request.url_root
        mail = request.json['email']
        username = request.json['username']
        if User.query.filter_by(mail=mail).first():
            return 2
        token = util.get_toekn(username, 600)
        msg = Message(subject='邮箱激活【小老师系统】',
                      recipients=[mail])
        msg.body = '您正在激活邮箱，请点击以下链接完成激活\n' + 'http://118.25.74.163' + url_for('api.email', mailtoken=token, mail=mail) + '\n【如果不是本人操作，请勿点击链接并请忽略】'
        try:
            util.send_mail(msg)
            return 1
        except:
            return 0
