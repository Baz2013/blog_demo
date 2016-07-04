from flask import Flask
from redis import Redis
import logging
from logging.handlers import RotatingFileHandler
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
#redis = Redis(host='123.57.14.82', port=9000)

def writeLog():
    global app
    file_handler = RotatingFileHandler('/var/log/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('{0} response'.format(socket.gethostname()))


@app.route('/')
def hello():
    redis.incr('hits')
    writeLog()
    return '<h1>Hello World! I have been seen %s times(%s).</h1>' % (redis.get('hits'), socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

