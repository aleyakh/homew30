import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from homework12.functions import search_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    key_word = request.args.get('s')
    logging.info('Выполняю поиск')
    try:
        posts = search_posts(key_word)
    except FileNotFoundError:
        logging.error('File not found')
        return 'File not found'
    except JSONDecodeError:
        return 'Not valid file'
    return render_template('post_list.html', result_post=posts, title=key_word)
