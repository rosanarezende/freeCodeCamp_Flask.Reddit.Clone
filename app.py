from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b8077ff7f73140:2a25c8b6@us-cdbr-east-02.cleardb.com/heroku_37fd418817fd19e'
db = SQLAlchemy(app)

@app.route('/')
def index():
  return 'Hello World!'

if __name__ == '__main__':
  app.run(debug=True)
