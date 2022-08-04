import json
import logging


def get_posts_all(): #возвращает посты
    with open('data/data.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):   #возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.
    result = []
    for name in get_posts_all():
        if user_name == name['poster_name']:
            result.append(name)
    return result


def get_comments_by_post_id(post_id):   #возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        result = []
        for comment in json.load(file):
            if post_id == comment['post_id']:
                result.append(comment)
        return result


def search_for_posts(query):    #возвращает список постов по ключевому слову
    result = []
    for keyword in get_posts_all():
        if query.lower() in keyword['content'].lower():
            if len(result) > 9:
                break
            result.append(keyword)
    return result


def get_post_by_pk(pk): #возвращает один пост по его идентификатору.
    pk_post = get_posts_all()
    return pk_post[pk-1]


def logs():
    logging.basicConfig(filename="logs/api.log", format='%(asctime)s [%(levelname)s] %(message)s')

