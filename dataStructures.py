# list data structure
mylist = ["toyota", "bmw", "subaru", "range", "nissan"]
mylist.append("mazda")
print(mylist)

# print(mylist[0])
mylist[1] = "mercedes"  # mutable
print(f"{mylist[1]} is manufactured in germany ")
print(mylist)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.insert(1, "orange")
print(list)
print(type(mylist))

# tuple data structure
mytuple = ("banana", "apple", "orange", "mangoes", "apples")
print(mytuple)
print(f"i love eating {mytuple[3]}")
# mytuple[2] = "watermelon"
# not mutable

# set data stracture
myset = {"kenya", "tz", "uk", "som"}
print(myset)
# myset[1] = "congo"
# not indexed

# dictionary data structure
mydict = {"name": "John", "age": 18, "gender": "male"}
print(mydict)
print(mydict["age"])
info = {"name": "abdi", "dob": 94, "gender": "male"}
print(f"my name is {info['name']} i was born in  {info['dob']} ,i am  {info['gender']}")
