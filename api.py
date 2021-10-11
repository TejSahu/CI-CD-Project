from flask import Flask, request
import json

app = Flask(__name__)

# Best Need for Speed Games
games = [{'id': 0,
            'title': 'Need for Speed Heat',
            'year_published': '2019'},
        {'id': 1,
            'title': 'Need for Speed Most Wanted',
            'published': '2005'},
        {'id': 2,
            'title': 'Need for Speed Underground 2',
            'published': '2004'}]

games_json = json.dumps(games)
@app.route('/')
def home():
    return '''<h1>Best Need for Speed titles</h1><p>API Sample returning best NFS Games</p>'''


@app.route('/games')
def games():
    return games_json

#app.run(host= '0.0.0.0')
app.run()

