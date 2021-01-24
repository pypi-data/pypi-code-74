from ext import EXT_CONTEXT
from sqlalchemy import Column, Integer, String

class User(EXT_CONTEXT["db"].Model):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    def __init__(self, name):
        self.name = name