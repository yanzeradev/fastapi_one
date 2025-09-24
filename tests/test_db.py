from dataclasses import asdict

from sqlalchemy import select

from fastapi_tcc.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User time=datetime.now()) as time:
        new_user = User(
            username='bob', email='bob@example.com', password='secret'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'bob'))

        assert user.username == 'bob'

        assert asdict(user) == {
            'id': 1,
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
            'created_at': time,
        }
