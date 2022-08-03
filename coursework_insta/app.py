from flask import Flask, render_template, request
from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

app = Flask(__name__)


@app.get('/')
def index_page():
    try:
        posts = get_posts_all()
    except FileNotFoundError:
        return 'Json файл не был найден'
    return render_template('index.html', posts=posts)


@app.get('/post/<int:pk_post>')
def post_page(pk_post):
    return render_template('post.html', post=get_post_by_pk(pk_post), comments=get_comments_by_post_id(pk_post))


@app.get('/search/')
def search_page():
    key_word = request.args.get('s')
    result_posts = search_for_posts(key_word)
    return render_template('search.html', title=key_word, posts=result_posts)


@app.get('/users/<string:user_post>')
def user_page(user_post):
    return render_template('user-feed.html', posts=get_posts_by_user(user_post))


@app.errorhandler(404)
def page_not_found(error):
    return "Ошибка 404 - Такой страницы не существует!", 404


@app.errorhandler(500)
def http_500_handler(error):
    return "Ошибка 500 - Ошибка на стороне сервера!", 500


if __name__ == '__main__':
    app.run(debug=True)
