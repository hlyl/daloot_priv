import sqlite3
from application import Item


class Database(object):
    def __init__(self, db_name):
        self.db_name = db_name

    '''
    CRUD Operations related to usages
    '''

    def create_item(self, item: Item):
        # database connection
        db_connection = sqlite3.connect(self.db_name)
        # sql statement
        sql_create_usage = "INSERT INTO usages(name,nominal,mean,restock,life_time,usage,tire,rarity,gun_type," \
                           "sub_type,mod,trader,dynamic_event,count_in_cargo,count_in_hoarder,count_in_map," \
                           "count_in_player) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
        # database cursor
        db_cursor = db_connection.cursor()
        db_cursor.execute(sql_create_usage, (item.get_name(), item.get_nominal(), item.get_mean(), item.get_restock(),
                                             item.get_life_time(), item.get_usage(), item.get_tire(), item.get_rarity(),
                                             item.get_type(), item.get_sub_type(), item.get_mod(), item.get_trader(),
                                             item.get_dynamic_event(), item.get_count_in_cargo(),
                                             item.get_count_in_hoarder(), item.get_count_in_map(),
                                             item.get_count_in_player()))
        db_connection.commit()
        db_connection.close()

    def update_item(self, usage_id, usage):
        pass

    def delete_item(self, usage_id):
        pass

    def all_items(self):
        pass
