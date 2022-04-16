"""
    (c) 2020 Rodney Maniego Jr.
    Maguro
"""

import statistics

class Maguro:
    def __init__(self, filepath="", delimiter=",", encoding="utf-8", autosave=True):
        """
            Read and prepare the list object.
            ...
            Parameters
            ---
            filepath: string
                path to save the file
            delimiter: string
                any string to delimit values
            autosave: boolean
                save list to file after every update
        """
        self.filepath = filepath
        self.delimiter = delimiter
        self.autosave = autosave
        self.encoding = encoding
        self.data = read(filepath, delimiter, encoding)
    
    def load(self, data):
        """
            Load and replace existing data with new list.
            ...
            Parameters
            ---
            data: list or iterable object
                a set of items that can be converted into a list
        """
        if iterable(data):
            self.data = list(data)
        if self.autosave:
            write(self.filepath, self.data, self.delimiter, self.encoding)
        return self
    
    def append(self, item):
        """ Append new item """
        self.data.append(str(item))
        if self.autosave:
            write(self.filepath, self.data, self.delimiter, self.encoding)
        return self
    
    def insert(self, index, item):
        """ Insert at index """
        try:
            self.data.insert(int(index), str(item))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter, self.encoding)
        except:
            pass
        return self
    
    def extend(self, collection):
        """ Extend the list """
        try:
            self.data.extend(list(collection))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter, self.encoding)
        except:
            pass
        return self
    
    def remove_duplicates(self):
        """ Remove duplicate items """
        try:
            self.data = list(set(self.data))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter, self.encoding)
        except:
            pass
        return self
    
    def unpack(self):
        """ Return raw list object """
        try:
            return self.data
        except:
            return []
    
    def pack(self):
        """ Return formmatted string """
        try:
            formatted = list([str(x) for x in self.data])
            return f"{self.delimiter}".join(formatted)
        except:
            return ""
    
    def pop(self, index):
        try:
            self.data.pop(int(index))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter, self.encoding)
        except:
            pass
        return self
    
    def remove(self, item):
        try:
            self.data = [x for x in self.data if x != str(item)]
            if self.autosave:
                write(self.filepath, self.data, self.delimiter, self.encoding)
        except:
            pass
        return self
    
    def sort(self, reverse=False):
        """ Sort the list, with optional reversal """
        self.data.sort(reverse=reverse)
        return self
    
    def reverse(self):
        """ Reverse the list """
        self.data.reverse()
        return self
    
    def items(self, sort=False, reverse=True):
        """ Loop over items """
        dataset = self.data
        try:
            if sort:
                dataset.sort(reverse)
        except:
            pass
        for item in dataset:
            yield item
    
    def contains(self, item):
        """
            Gets the value of the search key from the list.
            ...
            Parameters
            ---
            item: string
                item inside the list
                
        """
        if str(item) in self.data:
            return True
        return False
    
    def is_empty(self):
        """ Check if list is empty """
        if len(self.data) == 0:
            return True
        return False
    
    def is_not_empty(self):
        """ Check if list is not empty """
        if len(self.data) == 0:
            return False
        return True
    
    def count(self):
        """ Count the number of entries in the list """
        return len(self.data)
    
    def mean(self, precision=-1, fallback=None):
        """ Get the average of a numeric dataset """
        try:
            return precise(statistics.mean(self.data), precision)
        except:
            return fallback
    
    def median(self, precision=-1, fallback=None):
        """ Get the middle value of a numeric dataset """
        try:
            return precise(statistics.median(self.data), precision)
        except:
            return fallback
    
    def mode(self, precision=-1, fallback=None):
        """ Get the most frequent value in a numeric dataset """
        try:
            return precise(statistics.mode(self.data), precision)
        except:
            return fallback
    
    def dataset_range(self, precision=-1, fallback=None):
        """ Get the the difference of the min and max value of a numeric dataset """
        try:
            number = (max(self.data) - min(self.data))
            return precise(number, precision)
        except:
            return fallback
    
    def minimum(self, precision=-1, fallback=None):
        """ Get the the minimum value of a numeric dataset """
        try:
            return precise(min(self.data), precision)
        except:
            return fallback
    
    def maximum(self, precision=-1, fallback=None):
        """ Get the the minimum value of a numeric dataset """
        try:
            return precise(max(self.data), precision)
        except:
            return fallback
    
    def clear(self):
        self.data = []
        if self.autosave:
            write(self.filepath, self.data, self.delimiter, self.encoding)
        return self

def precise(number, precision=-1, fallback=None):
    try:
        if isinstance(precision, int) and 1 <= precision <= 16:
            if precision > 0:
                return round(number, precision)
        if precision == 0:
            return round(number)
    except:
        pass
    return number

def write(filepath, data, delimiter, encoding="utf-8"):
    if filepath != "":
        if iterable(data):
            try:
                with open(filepath, "w+", encoding=encoding) as file:
                    file.write(f"{delimiter}".join(data))
            except:
                pass

def iterable(data):
    try:
        it = iter(data)
    except:
        return False
    return True

def read(filepath, delimiter, encoding):
    try:
        with open(filepath, "r", encoding=encoding) as file:
            return list(file.read().split(delimiter))
    except:
        return []