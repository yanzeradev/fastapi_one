from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    assert response.json() == {'message': 'ola mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'email': 'bob@example.com', 'username': 'bob'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'yan',
            'email': 'yan@example.com',
            'password': 'senha',
        },
    )

    responseNF = client.put(
        '/users/-1',
        json={
            'username': 'yanNF',
            'email': 'yanNF@example.com',
            'password': 'senha',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'yan',
        'email': 'yan@example.com',
    }

    assert responseNF.status_code == HTTPStatus.NOT_FOUND


def test_get_user(client):
    response = client.get('/users/1')

    responseNF = client.get('/users/-1')
    assert response.json() == {
        'id': 1,
        'username': 'yan',
        'email': 'yan@example.com',
    }
    assert response.status_code == HTTPStatus.OK

    assert responseNF.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    responseNF = client.delete('/users/-1')
    assert response.json() == {
        'id': 1,
        'username': 'yan',
        'email': 'yan@example.com',
    }
    assert response.status_code == HTTPStatus.OK

    assert responseNF.status_code == HTTPStatus.NOT_FOUND
