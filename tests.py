from bakery import Bakery


def testBaking():
    bakery = Bakery()

    # Call the method to start the baking process and expect to see "Baking has started..."
    bakery.startBaking()

    # Call the method to increment the baking items and expect to see "Baking items"
    bakery.bakeItems()

    # Call the method to end the baking process and expect to see "Baking has finished..."
    bakery.endBaking()

    assert bakery.itemsBaked() == 1
