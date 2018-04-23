#python libs
import web
from pathlib import Path

#project files
import db


urls = (
  "", "input"
)

# terminology:
# entity: one game object
# instance: a specific players object in his/her game
#
# each entity needs a unique name
#
# requesttype=new
# nasal sends ?requesttype=new&callsign=pinto&ainame=static1&hp=50
# requesttype = type of request
# callsign = callsign of the person making the request. if default, make a random callsign
# ainame = name of the entity in-game
# hp = starting hp value
# if this is a new entity, set up said entity, create an instance ID, and set the
# hp value as requested.
# if this is not a new entity, then register a new instance and send the up-to-date
# hp value.
# if the callsign is already tied to an instance, return that instance number
# server returns instance_id=1; hp=50
#
# requesttype=pull
# nasal sends ?requesttype=pull&ainame=static1
# return the hp value of the entity
# server returns hp=50
#
# requesttype=push
# nasal sends ?requesttype=push&ainame=static1&hitvalue=10
# hitvalue = the amount of hp to subtract
#
# reqquesttype=delete
# nasal sends ?requesttype=delete&callsign=pinto&aiid=1
# aiid = id returned by requesttype=new
# free up an instance

class input:
    def GET(self):
        x = 3
        data = web.input()
        if not hasattr(data, 'requesttype'):
            return 'No requesttype specified, exiting.'
        if data.requesttype == 'new':
            new_request(data)
        elif data.requesttype == 'pull':
            pull_request(data)
        elif data.requesttype == 'push':
            push_request(data)
        elif data.requesttype == 'delete':
            delete_request(data)
        else:
           return 'Invalid requesttype, exiting.'

def new_request(data):
    ai_db = db.get_db()
    ai_c = db.get_connection()
#CREATE TABLE IF NOT EXISTS info (PRIMARY KEY id int, username text, password text)
app_static = web.application(urls, locals())
