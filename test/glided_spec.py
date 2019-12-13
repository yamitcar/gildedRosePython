from mamba import description, context, it
from expects import expect, equal
from gilded_rose.gilded_rose_wrapper import GildedRoseWrapper
from gilded_rose.gilded_rose import Item

VERSION = 'V2'

with description('GildedRose') as self:
    with it('should do nothing if it has no items'):
        items = []

        rose = GildedRoseWrapper(items,VERSION)
        rose.update_quality()

        expect(rose.items).to(equal(items))

    with it('should downgrade the quality and sell in of a generic item'):
        items = [Item(name="the name", quality=10, sell_in=10)]

        rose = GildedRoseWrapper(items,VERSION)
        rose.update_quality()

        expect(rose.items[0].quality).to(equal(9))
        expect(rose.items[0].sell_in).to(equal(9))

    with it('should not downgrade quality below 0'):
        items = [Item(name="the name", quality=0, sell_in=10)]

        rose = GildedRoseWrapper(items,VERSION)
        rose.update_quality()

        expect(rose.items[0].quality).to(equal(0))
        expect(rose.items[0].sell_in).to(equal(9))

    with context("Aged Brie"):
        with it("upgrades the quality of the item"):
            items = [Item(name="Aged Brie", quality=10, sell_in=10)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(11))
            expect(rose.items[0].sell_in).to(equal(9))

        with it("upgrades the quality by 2 after the sell in ends"):
            items = [Item(name="Aged Brie", quality=10, sell_in=0)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(12))
            expect(rose.items[0].sell_in).to(equal(-1))

        with it("tops at quality 50"):
            items = [Item(name="Aged Brie", quality=50, sell_in=0)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(50))
            expect(rose.items[0].sell_in).to(equal(-1))

    with context("Sulfuras"):
        with it("should not modify quality or sell in date"):
            items = [Item(name="Sulfuras, Hand of Ragnaros", quality=30, sell_in=10)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(30))
            expect(rose.items[0].sell_in).to(equal(10))
    with context("Backstage passes to a TAFKAL80ETC concert"):
        with it("should upgrade its quality by 1 when it have more than 10"):
            items = [Item(name="Backstage passes to a TAFKAL80ETC concert", quality=10, sell_in=12)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(11))
            expect(rose.items[0].sell_in).to(equal(11))

        with it("should upgrade its quality by 2 when it have more than 5 and less than 10 days"):
            items = [Item(name="Backstage passes to a TAFKAL80ETC concert", quality=10, sell_in=7)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(12))
            expect(rose.items[0].sell_in).to(equal(6))

        with it("should upgrade its quality by 3 when it have less than 5 days"):
            items = [Item(name="Backstage passes to a TAFKAL80ETC concert", quality=10, sell_in=2)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(13))
            expect(rose.items[0].sell_in).to(equal(1))

        with it("should downgrade its quality to 0 when it pass to selling date"):
            items = [Item(name="Backstage passes to a TAFKAL80ETC concert", quality=10, sell_in=0)]

            rose = GildedRoseWrapper(items,VERSION)
            rose.update_quality()

            expect(rose.items[0].quality).to(equal(0))
            expect(rose.items[0].sell_in).to(equal(-1))

    # with context("Conjured items"):
    #     with it("should downgrade its quality by 2"):
    #         items = [Item(name="Conjured Generic Item", quality=10, sell_in=10)]

    #         rose = GildedRoseWrapper(items,VERSION)
    #         rose.update_quality()

    #         expect(rose.items[0].quality).to(equal(8))
    #         expect(rose.items[0].sell_in).to(equal(9))