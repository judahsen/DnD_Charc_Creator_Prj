from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)


# Database

users = {
    '1': {
        'username': 'Brad G ',
        'email': 'brad@mail.com'
    },
    '2' : {
        'username': 'Quinn M',
        'email': 'quinn@mail.com'
    },
    '3' : {
        'username': 'Judah S',
        'email': 'judahs@mail.com'
    }
}

posts = {
    '1' : {
        'body' : {
          'name':'Glorblex',
          'race':'Plasmoid',
          'class':'Drunken Master Monk',
          'Level':'15'
        },
        'user_id': '1'
    },
    '2': {
        'body': {
          'name':'Raven',
          'race':'Fairy',
          'class':'COTM Druid',
          'Level':'5'
        },
        'user_id': '2'
    },
    '3':{
        'body': {
          'name':'Nicholas Adalbert',
          'race':'Fire Genasi',
          'class':'Barbarian',
          'Level':'8'
        },
        'user_id' : '3'
    }
}

# user routes

@app.get('/user')
def user():
  return { 'users': list(users.values()) }, 200

@app.route('/user', methods=["POST"])
def create_user():
  json_body = request.get_json()
  users[uuid4()] = json_body
  return { 'message' : f'{json_body["username"]} created' }, 201

@app.put('/user')
def update_user():
  return

@app.delete('/user')
def delete_user():
  pass



# post routes

@app.get('/post')
def get_posts():
  return

@app.post('/post')
def create_post():
  return

@app.put('/post')
def update_post():
  return

@app.delete('/post')
def delete_post():
  return