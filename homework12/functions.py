import json


def load_json():    # возвращает список всех кандидатов
    with open('posts2.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts(key_word): #возвращает найденные посты по ключевому слову
    result = []
    for post in load_json():
        if key_word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post):
    posts: list[dict] = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
