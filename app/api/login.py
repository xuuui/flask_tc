# -*-coding:utf-8 -*-
from flask import session
from flask_restful import Resource, request
from .util import get_toekn
from ..models import User as dbUser

class Auth(Resource):
    def get(self):
        return 'Hello'

    def post(self):
        username = request.json['username']
        password = request.json['password']
        u = dbUser.query.filter_by(username=username).first()
        if u:
            if dbUser.verify_pwd(self=u,password=password):
                token = get_toekn(username, 7200)
                return {'username':username,'activated': u.activated,'token':token}
            else:
                return {'username':username,'token':None}
        else:
            return {'username':u,'token':None}