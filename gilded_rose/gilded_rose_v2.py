# -*- coding: utf-8 -*-
from item.item_factory import ItemFactory

class GildedRoseV2(object):

    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = [ItemFactory.get(item) for item in items]

    def update_quality(self):
        for item in self.items:
            self.__update_quality_for_item(item)

    def __update_quality_for_item(self,item):
        if item.name == self.AGED_BRIE:
            return item.update()
        
        if item.name == self.BACKSTAGE:
            return self.__update_backstage(item)

        if item.name == self.SULFURAS:
            return self.__update_sulfuras(item)

        return self.__update_generic(item)  

    def __update_backstage(self, item):
        self.__increment_quality(item)
        if item.sell_in < 11:
            self.__increment_quality(item)
        if item.sell_in < 6:
            self.__increment_quality(item)
        self.__decrement_sell_in(item)
        if item.sell_in < 0:
            item.quality = item.quality - item.quality

    def __update_sulfuras(self, item):
        return

    def __update_generic(self, item):
        self.__decrement_quality(item)
        
        self.__decrement_sell_in(item)
        if item.sell_in < 0:
            self.__decrement_quality(item)

    def __increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def __decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def __decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)