class Fruits:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def onyesha(self):
        print(f"my favourite fruit is {self.name} and my price  is {self.price} and  its   {self.colour} in color")


Myobject = Fruits("oranges", 50, colour="orange")
Myobject2 = Fruits("apples", 60, colour="green")
Myobject3 = Fruits("bananas", 10, colour="yellow")

Myobject.onyesha()
Myobject2.onyesha()
Myobject3.onyesha()
