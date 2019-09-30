import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:passiwadi@localhost/posts'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'jessica'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'Nkujess@gmail.com'
    # QUOTES-API = 'http://quotes.stormconsultancy.co.uk/random.json'
    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True





    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
