# Define the class for our bakery
class Bakery:
    def __init__(self):
        self.items_baked = 0

    def startBaking(self):
        print("Baking has started...")

    def bakedItems(self):
        self.items_baked = self.items_baked + 1

    def endBaking(self):
        print("Baked has ended...")
        print("Total numbers of items baked: %d" % self.items_baked)
