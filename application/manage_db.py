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
        db_connection = sqlite3.connect(self.db_name)
        sql_create_update = "UPDATE items set name=?,nominal=?,mean=?,restock=?,life_time=?,usage=?,tire=?,rarity=?," \
                            "gun_type=?,sub_type=?,mod=?,trader=?,dynamic_event=?,count_in_cargo=?,count_in_hoarder=?," \
                            "count_in_map=?,count_in_player=? WHERE id=?"
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql_create_update, (item.get_name(), item.get_nominal(), item.get_mean(), item.get_restock(),
                                              item.get_life_time(), item.get_usage(), item.get_tire(),
                                              item.get_rarity(),
                                              item.get_type(), item.get_sub_type(), item.get_mod(), item.get_trader(),
                                              item.get_dynamic_event(), item.get_count_in_cargo(),
                                              item.get_count_in_hoarder(), item.get_count_in_map(),
                                              item.get_count_in_player(), item.get_item_id()))
        db_connection.commit()
        db_connection.close()

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
        db_connection = sqlite3.connect(self.db_name)
        db_cursor = db_connection.cursor()
        if item_sub_type is not None:
            sql_filter_items = "select * from items where item_type=? AND sub_type=?"
            db_cursor.execute(sql_filter_items, (item_type, item_sub_type))
        else:
            sql_filter_items = "select * from items where item_type=?"
            db_cursor.execute(sql_filter_items, (item_type,))
        items = db_cursor.fetchall()
        db_connection.commit()
        db_connection.close()
        return items
