import os
from math import ceil

from sqlalchemy import JSON, Boolean, Column, DateTime, Integer, String, create_engine
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


class GameHistory(Base):
    __tablename__ = "game_history"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    duration = Column(Integer)
    victory = Column(Boolean)
    ancient_id = Column(Integer)
    prologue_id = Column(Integer, nullable=True)
    rumors_id = Column(Integer, nullable=True)
    player_count = Column(Integer)
    investigators = Column(JSON)
    mysteries_solved = Column(Integer, nullable=True)
    gates_in_game = Column(Integer, nullable=True)
    monsters_in_game = Column(Integer, nullable=True)
    cules_in_game = Column(Integer, nullable=True)
    curses_in_game = Column(Integer, nullable=True)
    blessings_in_game = Column(Integer, nullable=True)
    rumors_in_game = Column(Integer, nullable=True)
    despair_level = Column(Integer)
    defeat_reason_id = Column(Integer, nullable=True)
    score = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)
    photos = Column(JSON, nullable=True)

    def __init__(
        self,
        date,
        duration,
        victory,
        ancient_id,
        player_count,
        investigators,
        despair_level,
        prologue_id,
        rumors_id,
        mysteries_solved,
        gates_in_game,
        monsters_in_game,
        cules_in_game,
        curses_in_game,
        blessings_in_game,
        rumors_in_game,
        defeat_reason_id,
        comment,
        photos,
    ):
        self.date = date
        self.duration = duration
        self.victory = victory
        self.ancient_id = ancient_id
        if prologue_id:
            self.prologue_id = prologue_id
        if rumors_id:
            self.rumors_id = rumors_id
        self.player_count = player_count
        self.investigators = investigators
        self.mysteries_solved = mysteries_solved
        if victory:
            if not gates_in_game:
                raise ValueError("gates_in_game is required for victory")
            self.gates_in_game = self.gates_in_game
            if not monsters_in_game:
                raise ValueError("monsters_in_game is required for victory")
            self.monsters_in_game = self.monsters_in_game
            if not curses_in_game:
                raise ValueError("curses_in_game is required for victory")
            self.curses_in_game = self.curses_in_game
            if not blessings_in_game:
                raise ValueError("blessings_in_game is required for victory")
            self.blessings_in_game = self.blessings_in_game
            if not rumors_in_game:
                raise ValueError("rumors_in_game is required for victory")
            self.rumors_in_game = self.rumors_in_game
            if not despair_level:
                raise ValueError("despair_level is required for victory")
            self.despair_level = despair_level
            score = 0
            score += gates_in_game
            score += ceil(monsters_in_game / 3)
            score += curses_in_game
            score += rumors_id * 3
            score -= ceil(cules_in_game / 3)
            score -= blessings_in_game
            score -= despair_level
            self.score = score
        else:
            if not defeat_reason_id:
                raise ValueError("defeat_reason_id is required for defeat")
            self.defeat_reason_id = defeat_reason_id
        self.comment = comment
        self.photos = photos


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


def create_game(
    date,
    duration,
    victory,
    ancient_id,
    player_count,
    investigators,
    despair_level,
    prologue_id=None,
    rumors_id=None,
    mysteries_solved=None,
    gates_in_game=None,
    monsters_in_game=None,
    cules_in_game=None,
    curses_in_game=None,
    blessings_in_game=None,
    rumors_in_game=None,
    defeat_reason_id=None,
    comment=None,
    photos=None,
):
    session = Session(engine)
    game = GameHistory(
        date=date,
        duration=duration,
        victory=victory,
        ancient_id=ancient_id,
        player_count=player_count,
        investigators=investigators,
        despair_level=despair_level,
        prologue_id=prologue_id,
        rumors_id=rumors_id,
        mysteries_solved=mysteries_solved,
        gates_in_game=gates_in_game,
        monsters_in_game=monsters_in_game,
        cules_in_game=cules_in_game,
        curses_in_game=curses_in_game,
        blessings_in_game=blessings_in_game,
        rumors_in_game=rumors_in_game,
        defeat_reason_id=defeat_reason_id,
        comment=comment,
        photos=photos,
    )
    session.add(game)
    session.commit()
    session.close()
    return
