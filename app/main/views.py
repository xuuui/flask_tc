from . import main

@main.route('/')
def index():
    return 'Hello'

@main.route('/email/<int:status>')
def mail(status):
    if status == 2:
        return '连接失效'
    return '成功' if status else '失败'