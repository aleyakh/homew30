import pytest

from app import app


def test_app():

    response = app.test_client().get('/api/posts')
    assert response.data == list, 'Ошибка - это не список'
