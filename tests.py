from maguro import Maguro


## Example #1
print("\nTest #1")
person = Maguro("tests.csv")
print(person.pack())


person = Maguro("tests.csv", delimiter=",", encoding="utf-8")
print(person.pack())

"""

# clear
person.clear()

# add items
person.append("Juan")
person.append("Male")
person.append("23")

# show
print(person.pack())

# raw list
print(person.unpack())

# loop over items
for item in person.items():
    print(item)

# remove item
person.remove("23")
person.append("24")
print(person.pack())

# insert item
person.insert(1, "Dela Cruz")
print(person.pack())

# load and replace original data with new one
maria = ["Doña Maria", "Concepion", "Female", "22"]
person.load(maria)
print(person.pack())
"""
