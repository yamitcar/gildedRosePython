from .gilded_rose import GildedRose
from .gilded_rose_v2 import GildedRoseV2


class GildedRoseFactory:

    @staticmethod
    def get(items, version='V2'):
        if version == 'V1':
            return GildedRose(items)
        else:
            return GildedRoseV2(items)

    