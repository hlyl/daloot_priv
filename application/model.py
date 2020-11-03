from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from application.db import Base


class Item(Base):
    __tablename__ = 'items'

    name = Column(String(50), primary_key=True)
    category = Column(String(45))
    type = Column(String)
    lifetime = Column(Integer)
    quantmin = Column(Integer, default=-1)
    nominal = Column(Integer, default=0)
    countmax = Column(Integer, default=-1)
    min_val = Column(Integer)
    cost = Column(Integer, default=100)
    restock = Column(Integer)
    Military = Column(Integer, default=0)
    Prison = Column(Integer, default=0)
    School = Column(Integer, default=0)
    Coast = Column(Integer, default=0)
    Village = Column(Integer, default=0)
    Industrial = Column(Integer, default=0)
    Medic = Column(Integer, default=0)
    Police = Column(Integer, default=0)
    Hunting = Column(Integer, default=0)
    Town = Column(Integer, default=0)
    Farm = Column(Integer, default=0)
    Firefighter = Column(Integer, default=0)
    Office = Column(Integer, default=0)
    Tier1 = Column(Integer, default=0)
    Tier2 = Column(Integer, default=0)
    Tier3 = Column(Integer, default=0)
    Tier4 = Column(Integer, default=0)
    floor = Column(Integer, default=0)
    shelves = Column(Integer, default=0)
    count_in_cargo = Column(Integer, default=0)
    count_in_hoarder = Column(Integer, default=0)
    count_in_map = Column(Integer, default=0)
    count_in_player = Column(Integer, default=0)
    crafted = Column(Integer, default=0)
    deloot = Column(Integer, default=0)
    ingame_name = Column(String, nullable=True)
    rarity = Column(Integer, default=0)
    mods = Column(String, default="Vanilla")
    subtype = Column(String, nullable=True)
    buyprice = Column(Integer, nullable=True)
    sellprice = Column(Integer, nullable=True)
    traderExclude = Column(Integer, default=0)
    traderCat = Column(String, nullable=True)
    trader_loc = Column(Integer)


class Combo(Base):
    __tablename__ = 'itemcombos'
    id = Column(Integer, primary_key=True, autoincrement=True)

    item1 = Column(Integer, ForeignKey("items.name"))
    item2 = Column(Integer, ForeignKey("items.name"))

    toone = relationship("Item", foreign_keys=[item1])
    tomany = relationship("Item", foreign_keys=[item2])
