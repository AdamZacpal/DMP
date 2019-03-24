import os

class KeyConfig():
    SECRET_KEY=b"rcKeEd5VAz3tKvpxVWf1ff5XrpsNZyeD"

class MySQLConfig():
    MYSQL_DATABASE_HOST="localhost"
    MYSQL_DATABASE_USER="root"
    MYSQL_DATABASE_PASSWORD="heslo"
    MYSQL_DATABASE_DB="myflaskapp"
    MYSQL_DATABASE_CURSORCLASS="DictCursor"


# Nastavení Mailu
class MailConfig():
    DEBUG=True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'zacpalweb@gmail.com'
    MAIL_PASSWORD = 'Fotbal123.'

regklic="123456"
