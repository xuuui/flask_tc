# -*-coding:utf-8 -*-
from flask_restful import Resource, request
from ..models import User as dbUser
from .util import  auth

class User(Resource):
    @auth.login_required
    def get(self):
        return 'ss'

    def post(self):
        username = request.json['username']
        password = request.json['password']
        if not dbUser.query.filter_by(username=username).first():
            v = dbUser(username=username,password=password,mail=None).save()
            if v:
                return {'status':1}
            else:
                return {'status':0}
        else:
            return {'status':2}

    @auth.login_required
    def delete(self):
        return ''

    @auth.login_required
    def put(self):
        return ''