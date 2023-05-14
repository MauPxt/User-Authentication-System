import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.user_model import UserDAO, User, Base
from src.utils.encryption_utils import decrypt_password

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


@pytest.fixture(scope='function')
def session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()
    Base.metadata.drop_all(engine)


class TestUserDAO:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, session):
        self.user_dao = UserDAO()
        yield
        session.query(User).delete()
        session.commit()

    def test_create_user(self, session):
        user_id = self.user_dao.create_user(
            username='test_user', password='password'
        )
        assert user_id is not None

        retrieved_user = self.user_dao.get_user_by_username('test_user')
        assert retrieved_user is not None
        assert retrieved_user.id == user_id
        assert retrieved_user.username == 'test_user'
        assert decrypt_password(retrieved_user.password, 'password') is True

    def test_create_duplicate_user(self, session):
        self.user_dao.create_user(username='test_user', password='password')

        user_id = self.user_dao.create_user(
            username='test_user', password='password'
        )
        assert user_id is None

    def test_create_user_with_empty_username(self, session):
        user_id = self.user_dao.create_user(username='', password='password')
        assert user_id is None

    def test_create_user_with_short_username_or_password(self, session):
        user_id = self.user_dao.create_user(username='test', password='short')
        assert user_id is None

        user_id = self.user_dao.create_user(
            username='short', password='password'
        )
        assert user_id is None

    def test_get_user_by_username(self, session):
        self.user_dao.create_user(username='test_user', password='password')

        retrieved_user = self.user_dao.get_user_by_username('test_user')

        assert retrieved_user is not None
        assert retrieved_user.username == 'test_user'
        assert decrypt_password(retrieved_user.password, 'password') is True

    def test_get_user_by_nonexistent_username(self, session):
        retrieved_user = self.user_dao.get_user_by_username('nonexistent')
        assert retrieved_user is None

    def test_delete_user(self, session):
        self.user_dao.create_user(username='test_user', password='password')

        result = self.user_dao.delete_user('test_user')
        assert result is True

        deleted_user = (
            session.query(User).filter_by(username='test_user').first()
        )
        assert deleted_user is None

    def test_delete_nonexistent_user(self, session):
        result = self.user_dao.delete_user('nonexistent')
        assert result is False


if __name__ == '__main__':
    pytest.main()
