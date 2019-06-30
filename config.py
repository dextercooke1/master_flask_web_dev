class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/dex"
    Debug = True