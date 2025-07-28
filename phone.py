from item import Item

class Phone(Item):
    all = []
    def __init__(self, name: str, price, quantity, broken_phones ):
        #call super functions
        super().__init__(
            name, price, quantity
        )
        
        self.broken_phones = broken_phones

        Phone.all.append(self)

