from bakery import Bakery


def testBakery():
    bakery = Bakery()

    # This will call the baking method and it will print out "Baking has started..."
    bakery.startBaking()

    # This will increment the the baking item counter
    bakery.bakedItems()

    # This will call the end baking method and it will print out "Baking has end..."
    bakery.endBaking()

    #
    assert bakery.bakedItems() == 1
