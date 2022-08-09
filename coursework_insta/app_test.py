import pytest

from app import app


def test_one():

    response = app.test_client().get('/api/posts')


    assert response.status_code == 200, 'Запрашиваемая страница не найдена'
    assert type(response.json) == list, 'Полученные данные не являются списком'

    keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for one_post in response.json:
        for key in keys:
            assert key in one_post, f"Ключ {key} не найден в посте {one_post['pk']}"


def test_two():

    response = app.test_client().get('/api/post/1')

    assert response.status_code == 200, 'Запрашиваемая страница не найдена'
    assert type(response.json) == dict, 'Полученные данные не являются словарем'

    keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for key in keys:
        assert key in response.json, f'Ключ {key} не найден в словаре'
