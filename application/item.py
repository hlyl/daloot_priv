from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nominal = Column(Integer)
    min = Column(Integer)
    restock = Column(Integer)
    lifetime = Column(Integer)
    usage = Column(String)
    tire = Column(String)
    rarity = Column(String)
    item_type = Column(String)
    sub_type = Column(String)
    mod = Column(String)
    trader = Column(Integer)
    dynamic_event = Column(Integer)
    count_in_cargo = Column(Integer)
    count_in_hoarder = Column(Integer)
    count_in_map = Column(Integer)
    count_in_player = Column(Integer)

    """def __init__(self, name, nominal, min_val, restock, lifetime, usage, tire, rarity, item_type, sub_type, mod, trader,
                 dynamic_event, count_in_hoarder, count_in_cargo, count_in_player, count_in_map):
        self.name = name
        self.nominal = nominal
        self.min = min_val
        self.restock = restock
        self.lifetime = lifetime
        self.usage = usage
        self.tire = tire
        self.rarity = rarity
        self.item_type = item_type
        self.sub_type = sub_type
        self.mod = mod
        self.trader = trader
        self.dynamic_event = dynamic_event
        self.count_in_hoarder = count_in_hoarder
        self.count_in_cargo = count_in_cargo
        self.count_in_player = count_in_player
        self.count_in_map = count_in_map
"""