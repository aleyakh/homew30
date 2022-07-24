import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from homework12.functions import add_post
from homework12.loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='template')

@loader_blueprint.route('/post')
def post_page_get():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_page_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Загруженный файл не картинка')
        return 'Bad file format'
    try:
        picture_path = save_picture(picture)
    except FileNotFoundError:
        logging.error('File not found')
        return 'File not found'
    except JSONDecodeError:
        return 'Not valid file'
    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', path=post)
