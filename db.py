import os

from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.orm import declarative_base, Session

DATABASE_URL = (f"postgresql://{os.getenv('POSTGRES_USER')}:"
                f"{os.getenv('POSTGRES_PASSWORD')}"
                f"@{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}/"
                f"{os.getenv('POSTGRES_DB')}")
Base = declarative_base()
engine = create_engine(DATABASE_URL)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    expansion=Column(Boolean)

    def __str__(self):
        return self.id


Base.metadata.create_all(engine)


def check_user_exists(user_id):
    if get_id_by_user_id(user_id):
        return True
    return False

def get_id_by_user_id(user_id):
    session = Session(engine)
    result = session.query(Users.id).filter_by(user_id=user_id).first()
    session.close()
    return result.id if result else None


def create_user(user_id):
    session = Session(engine)
    if not check_user_exists(user_id):
        user = Users(user_id=user_id)
        session.add(user)
    session.commit()
    session.close()


def get_all_users():
    session = Session(engine)
    result = list(str(user_id) for user_id in session.query(Users.user_id).all())
    if result:
        return result
    return []

def delete_user(user_id):
    session = Session(engine)
    session.query(Users).filter_by(user_id=user_id).delete()
    session.commit()
    session.close()
