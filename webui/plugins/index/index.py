import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/display")
