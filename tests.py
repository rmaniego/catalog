from karton import Karton


## Example #1
print("\nTest #1")
person = Karton("tests.csv")

# clear
person.clear()

# add items
person.append("Juan")
person.append("Male")
person.append("23")

# show
print(person.pack())
