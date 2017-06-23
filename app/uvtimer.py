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

    def __init__(self, variant, time, uvlevel):
        self.variant = variant
        self.time = time
        self.uvlevel = uvlevel

    def __repr__(self):
        return '<UV %r>' % (self.variant)

print UV

@app.route('/')
def index():
    return render_template("uvtimer.html")


@app.route('/store_time',methods=['GET','POST'])
def store_time():
    print request.json
    time = (int(request.json['min'])*60)+int(request.json['sec'])

    uv = UV(variant=request.json['variant'],time=time,uvlevel=int(request.json['uv']))

    print uv
    s.add(uv)
    s.commit()
    return render_template("uvtimer.html")

