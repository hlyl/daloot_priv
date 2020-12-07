import sqlite3
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from application import Item


class Database(object):
    def __init__(self, db_name):
        self.db_name = db_name
        engine = create_engine(f"sqlite:///{db_name}")
        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        self.session = session_maker()

    '''
    CRUD Operations related to items
    '''

    # create item
    def create_item(self, item: Item):
        self.session.add(item)
        self.session.commit()

    # update item
    def update_item(self, item: Item):
        pass

    # get item
    def get_item(self, item_id):
        item = self.session.query(Item).get(item_id)
        self.session.commit()
        return item

    # get items
    def all_items(self):
        """items = self.session.query(Item).all()
        self.session.commit()"""

        db_connection = sqlite3.connect(self.db_name)
        sql_delete_items = "select * from items"
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql_delete_items)
        items = db_cursor.fetchall()
        db_connection.commit()
        db_connection.close()
        return items

    # delete item
    def delete_item(self, item_id):
        item = self.session.query(Item).get(item_id)
        self.session.delete(item)
        self.session.commit()

    # delete items
    def delete_items(self):
        db_connection = sqlite3.connect(self.db_name)
        sql_delete_items = "delete from items"
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql_delete_items)
        db_connection.commit()
        db_connection.close()

    def filter_items(self, item_type, item_sub_type=None):
        if item_sub_type is not None:
            items = self.session.query(Item).filter(and_(Item.item_type == item_type, Item.sub_type == item_sub_type))
        else:
            items = self.session.query(Item).filter(Item.item_type == item_type)
        self.session.commit()
        return items
