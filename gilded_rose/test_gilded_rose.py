from gilded_rose.gilded_rose import GildedRose
from expects import expect, equal


class TestGildedRose:

    def test_zero(self):
        items = []
        rose = GildedRose(items)
        rose.update_quality()
        expect(rose.items).to(equal(items))

