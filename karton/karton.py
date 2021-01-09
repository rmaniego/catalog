"""
    (c) 2020 Rodney Maniego Jr.
    Karton
"""

class Karton:
    def __init__(self, filepath="", delimiter=",", autosave=True):
        """
            Read and prepare the JSON/list object.
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
    
    def append(self, item):
        """
            Formats and saves the list into a file.
            ...
            Parameters
            ---
            key: unique hashable string
                the key of the entry
            value: string, integer, float
                the value of the entry
        """
        self.data.append(item)
        if self.autosave:
            write(self.filepath, self.data, self.delimiter)
        return self
    
    def pack(self):
        return f"{self.delimiter}".join(self.data)
    
    def contains(self, value):
        """
            Gets the value of the search key from the  list.
            ...
            Parameters
            ---
            value: string
                item inside the list
                
        """
        if item in self.data:
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

def read(filepath, delimiter):
    try:
        with open(filepath, "r") as file:
            return file.read().split(delimiter)
    except:
        return []