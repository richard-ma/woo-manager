import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[WOO-MANAGER]'
    MAIL_SENDER = 'WOO-MANAGER Admin <app@example.com>'
    ADMIN = os.environ.get('app')
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    ORDERS_PER_PAGE = 20
    SITES_PER_PAGE = 50
    SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app, instance_path):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE = 'data-dev.sqlite'

    @classmethod
    def init_app(cls, app, instance_path):
        Config.init_app(app, instance_path)
        cls.SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                                  'sqlite:///' + os.path.join(instance_path, cls.SQLALCHEMY_DATABASE)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE = 'data.sqlite'

    @classmethod
    def init_app(cls, app, instance_path):
        Config.init_app(app, instance_path)

        cls.SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                                      'sqlite:///' + os.path.join(instance_path, cls.SQLALCHEMY_DATABASE)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.MAIL_SENDER,
            toaddrs=[cls.ADMIN],
            subject=cls.MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}