import gevent.monkey
gevent.monkey.patch_all()

bind = '127.0.0.1:5000'

reload = True
backlog = 2048
workers = 1
worker_class = 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker'
max_requests = 10000
keepalive = 5
pidfile = '/www/wwwroot/flask/logs/gunicorn.pid'
accesslog = '/www/wwwroot/flask/logs/access.log'
errorlog = '/www/wwwroot/flask/logs/error.log'
