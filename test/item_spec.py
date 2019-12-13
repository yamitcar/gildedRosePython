from mamba import description, context, it
from expects import expect, equal
from gilded_rose.gilded_rose import Item


with description('Item') as self:
  with it('should be initialized'):
    name = "the name"
    sell_in = 0
    quality = 0

    item = Item(name, sell_in, quality)
    
    expect(item.name).to(equal(name))
    expect(item.sell_in).to(equal(sell_in))
    expect(item.quality).to(equal(quality))

  
  with it('should have a string representation'):
    name = "the name"
    sell_in = 0
    quality = 0

    item = Item(name, sell_in, quality)
    
    expect(str(item)).to(equal(f"{name}, {sell_in}, {quality}"))


