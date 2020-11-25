class Item(object):
    def __init__(self):
        self.item_id = None
        self.name = None
        self.nominal = None
        self.mean = None
        self.restock = None
        self.life_time = None
        self.usage = None
        self.tire = None
        self.rarity = None
        self.type = None
        self.sub_type = None
        self.mod = None
        self.trader = None
        self.dynamic_event = None
        self.count_in_cargo = None
        self.count_in_hoarder = None
        self.count_in_map = None
        self.count_in_player = None

    # set item id
    def set_item_id(self, item_id):
        self.item_id = item_id

    # get item id
    def get_item_id(self):
        return self.item_id

    # set item name
    def set_name(self, name):
        self.name = name

    # get item name
    def get_name(self):
        return self.name

    # set nominal
    def set_nominal(self, nominal):
        self.nominal = nominal

    # get nominal
    def get_nominal(self):
        return self.nominal

    # set mean
    def set_mean(self, mean):
        self.mean = mean

    # get mean
    def get_mean(self):
        return self.mean

    # set restock
    def set_restock(self, restock):
        self.restock = restock

    # get restock
    def get_restock(self):
        return self.restock

    # set life_time
    def set_life_time(self, life_time):
        self.life_time = life_time

    # get life_time
    def get_life_time(self):
        return self.life_time

    # set usage
    def set_usage(self, usage):
        self.usage = usage

    # get usage
    def get_usage(self):
        return self.usage

    # set tire
    def set_tire(self, tire):
        self.tire = tire

    # get tire
    def get_tire(self):
        return self.tire

    # set rarity
    def set_rarity(self, rarity):
        self.rarity = rarity

    # get rarity

    def get_rarity(self):
        return self.rarity

    # set type
    def set_type(self, type):
        self.type = type

    # get type
    def get_type(self):
        return self.type

    # set sub_type
    def set_sub_type(self, sub_type):
        self.sub_type = sub_type

    # get sub_type
    def get_sub_type(self):
        return self.sub_type

    # set mod
    def set_mod(self, mod):
        self.mod = mod

    # get mod
    def get_mod(self):
        return self.mod

    # set trader
    def set_trader(self, trader):
        self.trader = trader

    # get trader
    def get_trader(self):
        return self.trader

    # set dynamic_event
    def set_dynamic_event(self, dynamic_event):
        self.dynamic_event = dynamic_event

    # get dynamic_event
    def get_dynamic_event(self):
        return self.dynamic_event

    # set count_in_cargo
    def set_count_in_cargo(self, count_in_cargo):
        self.count_in_cargo = count_in_cargo

    # get count_in_cargo
    def get_count_in_cargo(self):
        return self.count_in_cargo

    # set count_in_hoarder
    def set_count_in_hoarder(self, count_in_hoarder):
        self.count_in_hoarder = count_in_hoarder

    # get count_in_hoarder
    def get_count_in_hoarder(self):
        return self.count_in_hoarder

    # set count in map
    def set_count_in_map(self, count_in_map):
        self.count_in_map = count_in_map

    # get count in map
    def get_count_in_map(self):
        return self.count_in_map

    # set count in player
    def set_count_in_player(self, count_in_player):
        self.count_in_player = count_in_player

    # get count in player
    def get_count_in_player(self):
        return self.count_in_player
