from application import Config

config = Config("application/config.xml")

def test_config_getters():
  assert config.get_usages() == ['item1', 'item2', 'item3', 'item4']
  assert config.get_tires() == ['Tire 1', 'Tire 2', 'Tire 3']
  assert config.get_types() == ['all', 'type', 'type1', 'type2']
  assert config.get_rarities() == ['Rarity 1', 'Rarity 2']
  assert config.get_mods() == ['Mod 1', 'Mod 2']
  #TODO: add test of config.get_tree_heading()
  

