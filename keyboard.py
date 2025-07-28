from item import Item

class   Keyboard(Item):
    def __init__(self, name: str, price, quantity):
        #call super functions
        super().__init__(
            name, price, quantity
        )
   

