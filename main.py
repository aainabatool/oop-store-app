from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("My Item", 750, 10)

item1.name = "Other Item" #setter
print(item1.name)
#print(item1.read_only_name)

item1.apply_increment(0.2) #encapsulation
print(item1.price)

#item1.send_email() #abstarcation

item2 = Phone("jscPhone", 1000, 3, 1) #inheritance
item2. apply_increment(0.4)
print(item2.price)

item3 = Keyboard("jscKeyboard", 1000, 3) #polymorphism
item3. apply_discount()
print(item3.price)