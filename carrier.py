import web

urls = (
  "", "data"
)

class data:
    def GET(self):
	x = 3
	data = web.input()
        return data.foo

class carrier:
    def __init__():
        self.heading = heading
        self.speed = speed
        self.desired_heading = heading
        self.desired_speed = speed
	

def update_carrier_pos(carrierID, desired_heading, desired_speed):

app_carrier = web.application(urls, locals())
