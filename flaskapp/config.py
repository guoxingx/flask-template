# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class TextConfig(Config):
    DEBUG = True


config = {
    'test': TextConfig,
    'dev': DevelopmentConfig,
}
