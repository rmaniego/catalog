# Maguro
Maguro is a lightweight manager for delimiter-separated values.

### package import
from maguro import Maguro

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

### sorting
Use `dataset.sort()` to sort the list alphabetically.
Optional parameter: `reverse` = True | False *(default)*

### reverse
Use `dataset.reverse()` to reverse the list.

### remove item
Use `dataset.pop(value)` to to remove the first occurence in the list.

### to formatted string
Return a formatted string, concatenated by the specificied delimiter, by using `dataset.pack()` method.

### raw list
Return a raw list (of `list` data type) by using `dataset.unpack()` method.

### loop over items
When looping over a Maguro dataset, use `.items()` method to yield one item at a time.
Sort list: `sort` True | False *(default)*
Reverse list: `reverse`: True | False *(default)*
```python
for item in dataset.items():
    print(item)

for item in dataset.items(sort=True):
    print(item)

for item in dataset.items(sort=True, reverse=True):
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
Usage: `dataset.remove_duplicates()`

### numeric methods
The items in the dataset must be an integer or a float to get a valid result. The basic usage is `dataset.method()` or use `dataset.method(precision=2`) to define the number of decimal places.

**precision** = -1 (default), 0 = integer, 1 - 16 float

```python
numbers = Maguro("numbers.csv")
numbers.load([8.5,  0,  5,  14.2, 23.68,  -4,  -18,  12,  20])
print("Mean:", numbers.mean())
print("Mean (5 decimal places):", numbers.mean(precision=5))
print("Median:", numbers.median())
print("Mode:", numbers.mode())
print("Mode (whole number):", numbers.mode(precision=0))
print("Range:", numbers.dataset_range())
print("Minimum:", numbers.minimum())
print("Maximum:", numbers.maximum())
```
