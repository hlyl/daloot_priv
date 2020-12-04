from application import Config

config = Config("../../config.xml")
print("Usages")
print(config.get_usages())
print("Tires")
# print(config.get_tires())
print("Types")
print(config.get_types())
print("Rarities")
print(config.get_rarities())
print("Mods")
print(config.get_mods())
