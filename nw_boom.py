import web
urls = (
  "", "nw_boom"
)

class nw_boom:
    def GET(self):
	x = 3
	data = web.input()
        return data.foo

app_nw_boom = web.application(urls, locals())
