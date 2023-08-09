class Bakery:
    def __init__(self):
        self.itemsBaked = 0

    def startBaking(self):
        print("Baking has started...")

    def bakeItems(self):
        itemsBaked += 1
        print("Baking items...")

    def endBaking(self):
        print("Baking has finished...")
        print(f"Total number of items baked: {self.itemsBaked}")
