import os
# from dotenv import load_dotenv
# load_dotenv('.env')

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # секретный ключ для шифрования паролей
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'repsite'

    # настройка БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # настройка сервера
    SEND_FILE_MAX_AGE_DEFAULT = 0
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024

    # почта
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')

    # email, с которого будут приходить письма 
    FROM_EMAIL = os.environ.get('FROM_EMAIL')
