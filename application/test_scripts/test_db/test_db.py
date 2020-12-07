import pytest

from application import Database
from application import Item
from application import InitDatabase

DATABASE = 'test.db'

@pytest.fixture(scope='function')
def setup_db():
    database = InitDatabase(DATABASE)
    database.create_table()


def test_database_setters(setup_db):
    database = Database(DATABASE)
    # create item
    item = Item()

    item.set_name("Item_1")
    item.set_mean(12)
    item.set_nominal(9)
    item.set_restock(12)
    item.set_life_time(1212)
    item.set_usage("Test_Usage")
    item.set_tire("Tire_1")
    item.set_rarity("Very_rare")
    item.set_type("type2")
    item.set_sub_type("Sub Type")
    item.set_mod("Mod")
    item.set_trader(1)
    item.set_dynamic_event(1)
    item.set_count_in_cargo(1)
    item.set_count_in_hoarder(1)
    item.set_count_in_map(1)
    item.set_count_in_player(1)
    item.set_item_id(1)

    database.create_item(item)
    # database.delete_item(2)
    # database.delete_items()
    items = database.all_items()
    print(items)
    assert items[0] == (
    1, 'Item_1', 9, 12, 12, 1212, 'Test_Usage', 'Tire_1', 'Very_rare', 'type2', 'Sub Type', 'Mod', 1, 1, 1, 1, 1, 1)
