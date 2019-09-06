import os
import tornado.web
import tornado.ioloop
from settings import db

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        db.user.insert({'name':'cool','age':22})
        users = db.user.find().count()
        print users
        self.write("hello world!")

if __name__ == "__main__":
    settings = {
        'debug':True,
        'static_path':os.path.join(os.path.dirname(__file__),"static"),
        'template_path':os.path.join(os.path.dirname(__file__),"templates"),
    }

    application = tornado.web.Application([
        (r"/",MainHandler),#set the handler to handle the url request
    ],**settings)
    application.listen(9002)
    tornado.ioloop.IOLoop.instance().start()