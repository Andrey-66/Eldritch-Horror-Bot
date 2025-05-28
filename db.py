import os

from sqlalchemy import Boolean, Column, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

Base: DeclarativeBase = declarative_base()
engine = create_engine(DATABASE_URL)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    expansion_forsaken_lore = Column(Boolean, default=False)
    expansion_mountains_of_madness = Column(Boolean, default=False)
    expansion_strange_remnants = Column(Boolean, default=False)
    expansion_under_the_pyramids = Column(Boolean, default=False)
    expansion_signs_of_carcosa = Column(Boolean, default=False)
    expansion_the_dreamlands = Column(Boolean, default=False)
    expansion_cities_in_ruin = Column(Boolean, default=False)
    expansion_masks_of_nyarlathotep = Column(Boolean, default=False)

    def __init__(self, user_id):
        self.user_id = user_id
        self.expansion_forsaken_lore = False
        self.expansion_mountains_of_madness = False
        self.expansion_strange_remnants = False
        self.expansion_under_the_pyramids = False
        self.expansion_signs_of_carcosa = False
        self.expansion_the_dreamlands = False
        self.expansion_cities_in_ruin = False
        self.expansion_masks_of_nyarlathotep = False

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


def change_expansion(user_id, expansion):
    session = Session(engine)
    user = session.query(Users).filter_by(user_id=user_id).first()
    if expansion == "forsaken_lore":
        user.expansion_forsaken_lore = not user.expansion_forsaken_lore
    elif expansion == "mountains_of_madness":
        user.expansion_mountains_of_madness = not user.expansion_mountains_of_madness
    elif expansion == "strange_remnants":
        user.expansion_strange_remnants = not user.expansion_strange_remnants
    elif expansion == "under_the_pyramids":
        user.expansion_under_the_pyramids = not user.expansion_under_the_pyramids
    elif expansion == "signs_of_carcosa":
        user.expansion_signs_of_carcosa = not user.expansion_signs_of_carcosa
    elif expansion == "the_dreamlands":
        user.expansion_the_dreamlands = not user.expansion_the_dreamlands
    elif expansion == "cities_in_ruin":
        user.expansion_cities_in_ruin = not user.expansion_cities_in_ruin
    elif expansion == "masks_of_nyarlathotep":
        user.expansion_masks_of_nyarlathotep = not user.expansion_masks_of_nyarlathotep
    session.commit()
    session.close()


def check_expansion(user_id, expansion):
    session = Session(engine)
    user = session.query(Users).filter_by(user_id=user_id).first()
    if expansion == "forsaken_lore":
        result = user.expansion_forsaken_lore
        session.close()
        return result
    elif expansion == "mountains_of_madness":
        result = user.expansion_mountains_of_madness
        session.close()
        return result
    elif expansion == "strange_remnants":
        result = user.expansion_strange_remnants
        session.close()
        return result
    elif expansion == "under_the_pyramids":
        result = user.expansion_under_the_pyramids
        session.close()
        return result
    elif expansion == "signs_of_carcosa":
        result = user.expansion_signs_of_carcosa
        session.close()
        return result
    elif expansion == "the_dreamlands":
        result = user.expansion_the_dreamlands
        session.close()
        return result
    elif expansion == "cities_in_ruin":
        result = user.expansion_cities_in_ruin
        session.close()
        return result
    elif expansion == "masks_of_nyarlathotep":
        result = user.expansion_masks_of_nyarlathotep
        session.close()
        return result
    else:
        session.close()
        return None


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


def get_all_data():
    session = Session(engine)
    result = session.query(Users).all()
    session.close()
    return result
