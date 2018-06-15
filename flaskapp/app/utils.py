
import os

from werkzeug.datastructures import MultiDict
from flask import request


CONFIG = {}


def populate_config(config):
    """
    Generate config dict.
    """
    global CONFIG
    for key in dir(config):
        if key.isupper():
            CONFIG[key] = getattr(config, key)


def config_value(key):
    """
    Get config value.
    """
    global CONFIG
    return CONFIG.get(key)


def get_static_dir(child=None):
    """
    Return abs path of static dir.
    """
    abs_dir = os.path.dirname(__file__)
    res = '{}/static'.format(abs_dir)
    if child:
        res = '{}/{}'.format(res, child)
    return res


def remove_static_file(filename):
    """
    Remove file under static dir.
    """
    path = '{}/{}'.format(get_static_dir(), filename)
    try:
        os.system('rm {}'.format(path))
    except FileNotFoundError as e:
        print(e)


def save_static_file(fileStorage, filename):
    """
    Save file into static dir

    @param: filedata: <werkzeug.datastructures.FileStorage> e.g. request.files.get(key)
    """
    save_path = '{}/{}'.format(get_static_dir(), filename)
    fileStorage.save(save_path)


def get_form(form_class, _dict):
    """
    """
    data = {}
    for k, v in _dict.items():
        if v is not None:
            data[k] = v
    return form_class(MultiDict(data))


def form_by_json_request(form_class):
    """
    """
    return get_form(form_class, request.json or request.form)
