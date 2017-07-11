from flask import Flask
import app.config as config
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for, redirect

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'development key'
db = SQLAlchemy(app)
s = db.session

print db

class UV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant = db.Column(db.String(100), unique=False)
    time = db.Column(db.Integer)
    uvlevel = db.Column(db.Integer)
    type = db.Column(db.String(100), unique=False)

    def __init__(self, variant, time, uvlevel, type):
        self.variant = variant
        self.time = time
        self.uvlevel = uvlevel
        self.type = type

    def __repr__(self):
        return '<UV %r>' % (self.variant)

@app.route('/')
def index(message=None,modifier=None):
    return render_template("uvtimer.html",message=message,modifier=modifier)

@app.route('/store_time',methods=['POST','GET'])
def store_time():
    time = ((int(request.args['hours'])*60)*60)+(int(request.args['min'])*60)+int(request.args['sec'])
    print time
    uv = UV(variant=request.args['variant'],time=time,uvlevel=int(request.args['uv']),type=request.args['type'])
    s.add(uv)
    try:
        s.commit()
        message="Recorded that this UV"+request.args['uv']+" took "+request.args['hours']+":"+request.args['min']+":"+request.args['sec']
        modifier="success"
    except:
        message="Something went wrong "+request.args['uv']+" took "+request.args['hours']+":"+request.args['min']+":"+request.args['sec']
        modifier="danger"

    return render_template("uvtimer.html", message=message, modifier=modifier)


