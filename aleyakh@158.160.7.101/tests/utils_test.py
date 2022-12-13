import pytest

from utils import get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

#ТЕСТЫ ФУНКЦИИ get_posts_by_user


def test_get_posts_by_user_larry():
    user = get_posts_by_user('larry')
    assert len(user) > 0, 'Неверный вывод поста для larry'


def test_get_posts_by_user_marry():
    user = get_posts_by_user('marry')
    assert user == [], 'Неверный вывод поста для marry'


def test_get_posts_by_user_type_int():
    with pytest.raises(TypeError):
        get_posts_by_user(1)


def test_get_posts_by_user_type_float():
    with pytest.raises(TypeError):
        get_posts_by_user(1.5)

#ТЕСТЫ ФУНКЦИИ get_comments_by_post_id


def test_get_comments_by_post_id_one():
    comment_id = get_comments_by_post_id(1)
    assert len(comment_id) > 0, 'Неверный вывод коммента для 1'


def test_get_comments_by_post_id_ten():
    comment_id = get_comments_by_post_id(10)
    assert comment_id == [], 'Неверный вывод коммента для 10'


def test_get_comments_by_post_id_string():
    with pytest.raises(TypeError):
        get_comments_by_post_id('valera')


def test_get_comments_by_post_id_float():
    with pytest.raises(TypeError):
        get_comments_by_post_id(1.5)


#ТЕСТЫ ФУНКЦИИ search_for_posts


def test_search_for_posts_one():
    search_post = search_for_posts('кот')
    assert len(search_post) > 0, 'Неверный вывод поиска для кот'


def test_search_for_posts_null():
    search_post = search_for_posts('')
    assert len(search_post) > 0, 'Неверный вывод коммента для пустой строки'


#ТЕСТЫ ФУНКЦИИ get_post_by_pk


def test_get_post_by_pk_one():
    post_id = get_post_by_pk(1)
    assert len(post_id) > 0, 'Неверный вывод поста 1'


def test_get_post_by_pk_ten():
    post_id = get_post_by_pk(10)
    assert not post_id, 'Неверный вывод поста 10'


def test_get_post_by_pk_string():
    with pytest.raises(TypeError):
        get_post_by_pk('valera')


def test_get_post_by_pk_float():
    with pytest.raises(TypeError):
        get_post_by_pk(1.5)