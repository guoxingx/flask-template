
from . import main


@main.errorhandler(Exception)
def internal_server_error(e):
    raise e
