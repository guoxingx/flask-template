
import os

from flask import request, render_template, url_for

from . import main
from ..utils import save_static_file, get_static_dir


@main.route("/", methods=["GET", "POST"])
def index():
    images_dirname = 'images'

    if request.method == 'POST':
        image = request.files.get('image')
        filename = request.form.get('filename') or image.filename
        save_static_file(image, '{}/{}'.format(images_dirname, filename))

    image_list = os.listdir(get_image_dir(images_dirname))

    return render_template("index.html", image_list=image_list, image_url=image_url)


def image_url(filename):
    return url_for('static', filename='images/{}'.format(filename))


def get_image_dir(dirname):
    dirpath = get_static_dir(dirname)
    if not os.path.isdir(dirpath):
        os.system("mkdir -p {}".format(dirpath))
    return dirpath
