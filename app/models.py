from passlib.apps import custom_app_context as pwd_content
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    mail = db.Column(db.String(30), unique=True, index=True, nullable=True)
    activated = db.Column(db.Integer, default=0)

    def __init__(self, username, password, mail):
        self.username =username
        self.password_hash = pwd_content.encrypt(password)
        self.mail = mail

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def updata(self,password):
        self.password_hash = pwd_content.encrypt(password)
        db.session.commit()

    def user_active(self,activated):
        self.activated = activated
        db.session.commit()

    def verify_pwd(self, password):
        return pwd_content.verify(password, self.password_hash)

class Tokenused(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(150), index=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False