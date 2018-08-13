from flask import Blueprint
from flask_restful import Api

api = Blueprint('api', __name__)
rtf = Api(api)

from . import user, login, email, socket

rtf.add_resource(login.Auth,'/auth')
rtf.add_resource(user.User,'/user')
rtf.add_resource(email.Email,'/email','/email/<string:mailtoken>/<string:mail>')