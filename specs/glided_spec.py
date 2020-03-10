from mamba import description, it
from expects import expect, equal

from gilded_rose.gilded_rose import GildedRose

with description('GildedRose') as self:
    with it('should do nothing if it has no items'):
        items = []
        rose = GildedRose(items)
        rose.update_quality()
        expect(rose.items).to(equal(items))

