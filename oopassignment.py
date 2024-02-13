class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"my name is {self.name} and i am {self.age} years old")
person1 = People("John", 50)
person2 = People("Smith",70)
person3 = People("abdi",45)
person4 = People("mohamed",18)
person5 = People("fathi",25)

person1.display()
person2.display()
person3.display()
person4.display()
person5.display()
