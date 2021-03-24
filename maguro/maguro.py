"""
    (c) 2020 Rodney Maniego Jr.
    Maguro
"""

class Maguro:
    def __init__(self, filepath="", delimiter=",", autosave=True):
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
        self.data = read(filepath, delimiter)
    
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
            write(self.filepath, self.data, self.delimiter)
        return self
    
    def append(self, item):
        """ Append new item """
        self.data.append(str(item))
        if self.autosave:
            write(self.filepath, self.data, self.delimiter)
        return self
    
    def insert(self, index, item):
        """ Insert at index """
        try:
            self.data.insert(int(index), str(item))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter)
        except:
            pass
        return self
    
    def unpack(self):
        """ Return raw list object """
        return self.data
    
    def pack(self):
        """ Return formmatted string """
        return f"{self.delimiter}".join(self.data)
    
    def pop(self, index):
        try:
            self.data.pop(int(index))
            if self.autosave:
                write(self.filepath, self.data, self.delimiter)
        except:
            pass
        return self
    
    def remove(self, item):
        try:
            self.data = [x for x in self.data if x != str(item)]
            if self.autosave:
                write(self.filepath, self.data, self.delimiter)
        except:
            pass
        return self
    
    def items(self):
        """ Loop over items """
        for item in self.data:
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
    
    def clear(self):
        self.data = []
        if self.autosave:
            write(self.filepath, self.data, self.delimiter)
        return self

def write(filepath, data, delimiter):
    if filepath != "":
        if iterable(data):
            try:
                with open(filepath, "w+") as file:
                    file.write(f"{delimiter}".join(data))
            except:
                pass

def iterable(data):
    try:
        it = iter(data)
    except:
        return False
    return True

def read(filepath, delimiter, encoding="utf-8", retry=0):
    try:
        with open(filepath, "r", encoding=encoding) as file:
            return file.read().split(delimiter)
    except:
        if retry < 2:
            retry += 1
            return read(filepath, delimiter, encoding="latin-1", retry=retry)
        return []