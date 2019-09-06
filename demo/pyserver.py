#coding=utf-8
from wsgiref.simple_server import make_server
import webbrowser
from StringIO import StringIO

def demo_app(environ,start_response):
    stdout = StringIO()
    print >>stdout, "Hello NJUPT!%s"%environ['PATH_INFO']
    print >>stdout
    # h = environ.items(); 
    # h.sort()
    # for k,v in h:
    #     print >>stdout, k,'=', repr(v)
    start_response("200 OK", [('Content-Type','text/plain')])
    return [stdout.getvalue()]


if __name__ == '__main__':
    httpd = make_server('',9001,demo_app)
    sa = httpd.socket.getsockname()
    webbrowser.open('http://localhost:9001/xyz?abc')
    # httpd.handle_request() #单次处理调用
    httpd.serve_forever()