from xml.dom import minidom


class Config(object):
    def __init__(self, config_file):
        self.config_file = minidom.parse(config_file)

    def get_usages(self):
        usage_list = self.config_file.getElementsByTagName('usage')
        usages = list()
        for i in usage_list:
            usages.append(i.attributes['value'].value)
        return usages

    def get_types(self):
        type_list = self.config_file.getElementsByTagName('type')
        types = list()
        for i in type_list:
            types.append(i.attributes['value'].value)

        return types

    def get_tires(self):
        tire_list = self.config_file.getElementsByTagName('tire')
        tires = list()
        for i in tire_list:
            tires.append(i.attributes['value'].value)
        return tires

    def get_mods(self):
        mod_list = self.config_file.getElementsByTagName('mod')
        mods = list()
        for i in mod_list:
            mods.append(i.attributes['value'].value)
        return mods

    def get_rarities(self):
        rarity_list = self.config_file.getElementsByTagName('rarity')
        rarities = list()
        for i in rarity_list:
            rarities.append(i.attributes['value'].value)
        return rarities
