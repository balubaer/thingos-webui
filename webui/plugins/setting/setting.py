import tornado.web

class SettingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("setting.html", title="Setting")
