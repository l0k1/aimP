import web
from pathlib import Path
#import nw_boom
import static

aimP_folder = str(Path.home()) + "/.aimp"
aimP_database = aimP_folder + "/aidb.sqlite"

urls = (
#	'/(.+)', 'index',
#	'/nw_boom', nw_boom.app_nw_boom
	'/static', static.app_static,
)

class index:
    def GET(self):
        data = web.input()
        return data.foo

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
