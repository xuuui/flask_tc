import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'xlsFx'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEFAULT_SENDER = '846783775@qq.com'
    MAIL_USERNAME = '846783775@qq.com'
    MAIL_PASSWORD = 'fsrtfrqfilvmbcjc'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://fxFlask:fangruiyi@118.25.74.163:3306/fxFlask?charset=utf8"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://fxFlask:fangruiyi@127.0.0.1:3306/fxFlask?charset=utf8"


config={
        'Development':DevelopmentConfig,
        'Production':ProductionConfig
        }