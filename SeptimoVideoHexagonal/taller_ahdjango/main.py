from wsgiref import simple_server
from ah_django.wsgi import application

if __name__ == '__main__':
    server = simple_server.make_server(host='localhost', app=application, port=8888)
    server.serve_forever()