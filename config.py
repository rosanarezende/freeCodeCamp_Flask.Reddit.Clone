class Config(object):
  DEBUG = False
  TESTING = False

  db_username = 'b8077ff7f73140'
  db_password = '2a25c8b6'
  db_host     = 'us-cdbr-east-02.cleardb.com'
  db_db       = 'heroku_37fd418817fd19e'

  SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_db)

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG = True
