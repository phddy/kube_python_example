import application
from wsgiref import simple_server

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, application.app)
    httpd.serve_forever()
