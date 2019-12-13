from .item_v2 import ItemV2

class AgedBrie(ItemV2):
    def update(self):
        self.increment_quality()
        self.decrement_sell_in()

        if self.sell_in < 0:
            self.increment_quality()