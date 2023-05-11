from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class UserDAO:
    def __init__(self):
        self.session = Session()

        if not inspect(engine).has_table('users'):
            Base.metadata.create_all(engine)

    def create_user(self, username, password):
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()
        return user.id

    def get_user_by_username(self, username):
        user = self.session.query(User).filter_by(username=username).first()
        return user

    def delete_user(self, username):
        result = self.session.query(User).filter_by(username=username).delete()
        self.session.commit()
        return result == 1


if __name__ == '__main__':
    if not inspect(engine).has_table('users'):
        Base.metadata.create_all(engine)

    # user_dao = UserDAO()
    # user_dao.delete_user('test_user')
