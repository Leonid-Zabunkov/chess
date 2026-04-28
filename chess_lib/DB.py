import random

from sqlalchemy import create_engine, Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class ChessPuzzle(Base):
    __tablename__ = 'puzzles'
    
    id = Column(Integer, primary_key=True)
    white_turn = Column(Boolean)
    board = Column(String)
    moves_to_win = Column(Integer)
    solution = Column(JSON)

# Настройка базы
engine = create_engine('sqlite:///chess_puzzles.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_sample_puzzles():
    session.add(ChessPuzzle(
        white_turn=True,
        board="--------/--------/--------/--------/--------/qk------/--------/-K------",
        moves_to_win=1,
        solution=["a6-b7"]
    ))
    session.add(ChessPuzzle(
        white_turn=True,
        board="--------/--------/--------/-----q--/--------/-k------/--------/--K-----",
        moves_to_win=1,
        solution=["f4-c7"]
    ))
    session.commit()

def get_random_puzzle():
    count = session.query(ChessPuzzle).count()
    return get_puzzle(random.randint(1, count))

def get_puzzle(index: int):
    return session.query(ChessPuzzle).get(index)
