#coding=utf8
from flask import Flask
from datetime import datetime
from flask import current_app
from flask import g
app = Flask(__name__)
ctx=app.app_context()
ctx.push()

ServerPort=7333 # 服务端口号
g.LastIP=''
g.LastUpdataTime=''
@app.route('/')
def Index():
    s='%s      %s' % (g.LastIP,g.LastUpdataTime)
    return '%s      %s' % (g.LastIP,g.LastUpdataTime)

@app.route('/updata/<ip>', methods=['GET'])
def update(ip):
    g.LastIP=ip
    g.LastUpdataTime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=ServerPort)