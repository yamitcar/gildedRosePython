from .item_v2 import ItemV2
from .aged_brie_item import AgedBrie

class ItemFactory:

    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    @classmethod
    def get(cls, item):
        if item.name == cls.AGED_BRIE:
            return AgedBrie(item.name, item.sell_in, item.quality)
        else:
            return item
        