from gilded_rose.gilded_rose_factory import GildedRoseFactory

class GildedRoseWrapper:

    def __init__(self, items, version='V2'):
        self.gilded_rose = GildedRoseFactory.get(items, version)

    def update_quality(self):
        return self.gilded_rose.update_quality()

    @property
    def items(self):
        return self.gilded_rose.items