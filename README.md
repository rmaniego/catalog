# Maguro

Maguro is a Python-wrapper for DSV files.

Other behaviors are similar to a native Python list, the tutorial below only covers add-on features specific to Maguro.

# Official Release

Maguro can now be used on your Python projects through PyPi by running pip command on a Python-ready environment.

`pip install maguro --upgrade`

Current version is 1.1.0, but more updates are coming soon. This is compatible with Python version 3.9 or with the latest.

### package import
`from maguro import Maguro`

### basic usage
```python
dataset = Maguro("dataset.csv")
```

### custom encoding
```python
dataset = Maguro("dataset.csv", encoding="utf-8")
```

### custom delimiter
```python
dataset = Maguro("dataset.tsv", delimiter="\t")
```

### clear
Remove all items inside the list by using `dataset.clear()` method.

### add items
Use `dataset.append(value)` to add new item in the list.


### add only if unique
Use `dataset.append(value, unique=True)` to add if item is not yet in the list.

### sorting
Use `dataset.sort()` to sort the list alphabetically.

### reverse
Use `dataset.reverse()` to reverse the list.

### remove item
Use `dataset.pop(index)` to to remove the first occurence in the list.

### to formatted string
Return a formatted string, concatenated by the specificied delimiter, by using `dataset.pack()` method.

### raw list
Return a raw list (of `list` data type) by using `dataset.unpack()` method.

### loop over items
```python
for item in dataset:
    print(item)
```

### remove item
Remove existing (or non-existing) value.
Usage: `dataset.remove(value)`

### insert item
Insert data at a specific index
Usage: `dataset.insert(index, value)`

### load list
Loading new data into a Maguro object will replace previous contents.
Usage: `dataset.load(iterable)`

### extend list
Extending original lists follows the same list syntax.
Usage: `dataset.extend(iterable)`

### remove duplicates
Maguro leverages Python `list(set())` casting to remove duplicates.
Usage: `dataset.distinct()`

### Creating 2D arrays
```python
test = Maguro("temp/03b-2d.csv", delimiter=",", newline="\n")
test.append(["Juan", 23, "Male", 72, 168, False])
test.append(["Pedro", 22, "Male", 68, 172, True])
test.append(["Maria", 19, "Female", 56, 162, True])
````

### Force Quotations on Strings
```python
test = Maguro("temp/9-tab-separated-values.tsv", delimiter="\t", newline="\n", quote_strings=True)
test.clear()
test.append(["a", "b", "c", "d", "e"])
test.append(["1", "2", "3", "4", "5"])
test.append([1, 2, 3, 4, 5])

print(test.unpack())
````

### Convert `Yes`, `y`, `No`, and `n` to Boolean data type (run-time only)
```python
test = Maguro("temp/04-booleans.csv", delimiter=",", newline="\n", allow_boolean=True)
````