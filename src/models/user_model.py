import re
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import inspect, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.utils.encryption_utils import encrypt_password

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class UserDAO:
    def __init__(self):
        self.session = Session()
        Base.metadata.create_all(engine, checkfirst=True)

    def create_user(self, username, password):
        if not self._is_valid_input(username, password):
            return None

        encrypted_password = encrypt_password(password)

        try:
            user = User(username=username, password=encrypted_password)
            self.session.add(user)
            self.session.commit()
            return user.id
        except exc.SQLAlchemyError as e:
            self.session.rollback()
            print(f'Error creating user: {e}')
            return None

    def get_user_by_username(self, username):
        if not self._is_valid_input(username):
            return None

        return (
            self.session.query(User).filter(User.username == username).first()
        )

    def delete_user(self, username):
        if not self._is_valid_input(username):
            return None

        try:
            user = (
                self.session.query(User)
                .filter(User.username == username)
                .first()
            )
            if user:
                self.session.delete(user)
                self.session.commit()
                return True
            else:
                return False
        except exc.SQLAlchemyError as e:
            self.session.rollback()
            print(f'Error deleting user: {e}')
            return False

    def _is_valid_input(self, username=None, password=None):
        pattern = re.compile(r'^[a-zA-Z0-9_]{8,20}$')
        if username is not None and (
            not username or not pattern.match(username)
        ):
            return False
        if password is not None and (
            not password or not pattern.match(password)
        ):
            return False
        return True


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)
    # user_dao = UserDAO()
    # user_dao.delete_user('test_user')
