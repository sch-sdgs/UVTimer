import os
basedir = os.path.dirname(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/resources/uv.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:////resources/uv.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'resources')
SQLALCHEMY_MIGRATE_REPO = '/resources'