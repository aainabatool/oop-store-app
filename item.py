import csv

class Item:
    all = []
    pay_rate = 0.8 #thw pay_rate after 20% discount
    def __init__(self, name: str, price, quantity):

        assert price >= 0, f"Price{price} must be greater than equal to zero"
        assert quantity >= 0

        self.__name = name
        self.__price = price  #encapsulation
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property   #encapsulation
    def price(self):
        return self.__price
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property           
    def name(self):
        return self.__name

    @name.setter            #setter
    def name(self, value):
        self.__name = value


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items= list(reader)

        for item in items:
            #print(item)
            Item(
                name=item.get('name'), 
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))

            )

    def __repr__(self):
        return f"Item('{self.name}', {self.__price}, {self.quantity})"
    
    def __connect(self, smpt_server): #abstraction
        pass

    def __prepare_body(self):
        return f"""
        Hello Aaina.
        We have {self.name} {self.quantity} times.
        Regards, HexCoding
        """
    
    def __send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    
    #@property
    #def read_only_name(self):
        #return "AAA" 

Item.instantiate_from_csv()
