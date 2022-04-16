from maguro import Maguro


print("\nTest #1a Initialization")
test = Maguro("temp/01a-initialization.csv")

print("\nTest #1b Auto Save = False")
test = Maguro("temp/01b-auto-save-no.csv", autosave=False)
for x in range(100):
    test.append(x, unique=True)
test.save() # save to initialized filepath
# save as new file
test.append(100, unique=True)
test.append(100)
test.append(100)
test.save(save_as="temp/01b-auto-save-new.csv")

print("\nTest #2a Native Set/Get")
test = Maguro("temp/02a-native-methods.csv")
test.append("Juan")
test[0] = "Pedro"
print(test[0])

print("\nTest #2b Native Clear")
test = Maguro("temp/02b-native-clear.csv")
test.append("Juan")
test.clear()
test.append("Pedro")
print(test.pack())

print("\nTest #2c Native Extend")
test = Maguro("temp/02c-native-extend.csv")
test.clear()
test.append("Juan")
test.extend(["Pedro", "Maria"])
print(test.pack())

print("\nTest #2d Native Insert")
test = Maguro("temp/02d-native-insert.csv")
test.clear()
test.append("Juan")
test.extend(["Pedro", "Maria"])
test.insert(1, "Soledad")
print(test.pack())

print("\nTest #2e Native Pop")
test = Maguro("temp/02e-native-pop.csv")
test.clear()
test.extend(["Juan", "Pedro", "Maria"])
temp = test.pop(2)
print(" - Pop:", temp)

print("\nTest #2f Native Remove")
test = Maguro("temp/02f-native-remove.csv")
test.clear()
test.extend(["Juan", "Pedro", "Maria"])
test.remove("Pedro")
print(test.pack())

print("\nTest #2g Native Reverse")
test = Maguro("temp/02g-native-remove.csv")
test.clear()
test.extend(["Juan", "Pedro", "Maria"])
test.reverse()
print(test.pack())

print("\nTest #2h Native Sort")
test = Maguro("temp/02g-native-sort.csv")
test.clear()
test.extend(["Juan", "Pedro", "Maria"])
test.sort()
print(test.pack())

print("\nTest #3a 1D array")
test = Maguro("temp/03a-1d.csv", delimiter=",")
print(test.unpack())

print("\nTest #3b 2D array")
test = Maguro("temp/03b-2d.csv", delimiter=",", newline="\n")
print(test.unpack())

print("\nTest #3c Mixed-data 2D array")
test = Maguro("temp/03c-2d-mixed.csv", delimiter=",", newline="\n")
print(test.unpack())

print("\nTest #4 Booleans")
test = Maguro("temp/04-booleans.csv", delimiter=",", newline="\n", allow_boolean=True)
print(test.unpack())

print("\nTest #5a NaNs")
test = Maguro("temp/05a-NaNs.csv", delimiter=",", newline="\n")
print(test.unpack())

print("\nTest #5b NaNs as ''")
test = Maguro("temp/05b-NaNs.csv", delimiter=",", newline="\n", NaN="")
print(test.unpack())

print("\nTest #5c NaNs as 0")
test = Maguro("temp/05c-NaNs.csv", delimiter=",", newline="\n", NaN=0)
print(test.unpack())

print("\nTest #6 Format to DSV")
test = Maguro("temp/06-format-to-dsv.csv", delimiter=",", newline="\n")
print(test.pack())

print("\nTest #7 Remove Duplicates")
test = Maguro("temp/07-distinct.csv")
test.clear()
test.extend(["Juan", "Pedro", "Maria", 1, "2", 2])
test.append("Juan")
test.distinct()
print(test.unpack())

print("\nTest #8 Check if Empty or Not")
test = Maguro("temp/8-is-empty.csv")
test.clear()
print("Empty: ", test.is_empty())
test.extend(["Juan", "Pedro", "Maria", 1, "2", 2])
print("Empty: ", test.is_empty())

print("\nTest #9 TSV file")
test = Maguro("temp/9-tab-separated-values.tsv", delimiter="\t", newline="\n", quote_strings=True)
test.clear()
test.append(["a", "b", "c", "d", "e"])
test.append(["1", "2", "3", "4", "5"])
test.append([1, 2, 3, 4, 5])
print(test.unpack())

print("\nTest #10 Load and replace new contents.")
test = Maguro("temp/10-load-list.tsv", delimiter="\t", newline="\n", quote_strings=True)
test.clear()
test.append(["a", "b", "c", "d", "e"])
print("Test:", test.unpack())
test.load([["1", "2", "3", "4", "5"]])
print("Test:",test.unpack())