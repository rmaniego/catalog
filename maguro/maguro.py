"""
    (c) 2020 Rodney Maniego Jr.
    Maguro
"""

import shlex
import threading

class Maguro(list):
    """ Parse DSV files into a 2D Python array. """
    def __init__(self, filepath=None, delimiter=",", newline=None, encoding="utf-8", autosave=True, quote_strings=False, allow_boolean=False, NaN="NaN"):
        self._lock = threading.RLock()
        with self._lock:
            self._filepath = filepath
            self._delimiter = delimiter
            self._newline = newline
            self._autosave = autosave
            self._quote_strings = quote_strings
            self._encoding = encoding
            self._allow_boolean = allow_boolean
            self._packed = None
            self._NaN = NaN # None
            self.extend(_read_file(self))
    
    def __setitem__(self, index, item):
        with self._lock:
            self._packed = None
            if isinstance(item, (list, set, tuple)):
                item = list(item)
            super(Maguro, self).__setitem__(index, item)
            
            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def append(self, item, unique=False):
        with self._lock:
            self._packed = None
            if isinstance(item, (list, set, tuple)):
                item = list(item)
            if not unique or (item not in self):
                super(Maguro, self).append(item)

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def clear(self):
        with self._lock:
            self._packed = None
            super(Maguro, self).clear()

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def extend(self, iterable):
        with self._lock:
            self._packed = None
            super(Maguro, self).extend(iterable)

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def insert(self, index, item):
        with self._lock:
            self._packed = None
            super(Maguro, self).insert(index, item)

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def pop(self, pos):
        with self._lock:
            self._packed = None
            temp = super(Maguro, self).pop(pos)

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
            return temp
    
    def remove(self, item):
        with self._lock:
            self._packed = None
            super(Maguro, self).remove(item)

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def reverse(self):
        with self._lock:
            self._packed = None
            super(Maguro, self).reverse()

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def sort(self):
        with self._lock:
            self._packed = None
            super(Maguro, self).sort()

            autosave = isinstance(self._autosave, bool) and bool(self._autosave)
            if autosave:
                _write_file(self)
    
    def load(self, iterable):
        """ Replace old data with new contents. """
        with self._lock:
            self._packed = None
            if isinstance(iterable, (list, set, tuple)):
                try:
                    self.clear()
                    self.extend(list(iterable))

                    autosave = isinstance(self._autosave, bool) and bool(self._autosave)
                    if autosave:
                        _write_file(self)
                except:
                    pass
    
    def distinct(self):
        """ Remove duplicates on lists with hashable contents. """
        with self._lock:
            self._packed = None
            try:
                temp = list(set(self))
                self.clear()
                self.extend(temp)

                autosave = isinstance(self._autosave, bool) and bool(self._autosave)
                if autosave:
                    _write_file(self)
            except:
                pass
    
    def is_empty(self):
        """ Check if list object is empty or not. """
        with self._lock:
            return not len(self)

    def pack(self):
        """ Return delimiter-separates values in string representation. """
        with self._lock:
            self._packed = _pack(self)
            return self._packed
    
    def unpack(self):
        """ Return raw list object """
        with self._lock:
            return list(self)
    
    def save(self, save_as=None):
        """ Manual save to optimize operations. """
        with self._lock:
            if isinstance(save_as, str):
                self._filepath = save_as
            _write_file(self)

def _encode_dsv_equivalent(value, separator, quote_strings):
    """ Encode values into formatted string representations. """
    if value is None:
        return "null"
    if value == "NaN":
        return "NaN"
    if type(value) in (int, float):
        return value
    if isinstance(value, bool):
        if value:
            return "Yes"
        return "No"
    formatted = f"\"{value}\""
    if quote_strings:
        return formatted
    if separator is not None:
        if separator in value:
            return formatted
    if " " in value:
        return formatted
    return value

def _pack(data):
    """ Convert list object into delimiter-separated values representation. """
    if not isinstance(data._delimiter, str):
        return
    sep1 = data._delimiter
    sep2 = None
    if isinstance(data._newline, str):
        sep1 = data._newline
        sep2 = data._delimiter

    formatted = []
    quote_strings = isinstance(data._quote_strings, bool) and bool(data._quote_strings)
    for value in list(data):
        if sep2 is None:
            formatted.append(str(_encode_dsv_equivalent(value, sep1, quote_strings)))
            continue
        temp = []
        for part in value:
            temp.append(str(_encode_dsv_equivalent(part, sep2, quote_strings)))
        formatted.append(sep2.join(temp))
    return sep1.join(formatted)

def _clean_split(string, separator, allow_boolean, NaN):
    """ Smartly split valid strings outside quuted values. """
    formatted = string.replace(" ", "&nbsp;")
    formatted = formatted.replace(separator, "    &tmp;")
    parts = list(shlex.split(formatted))
    for i in range(len(parts)):
        temp = parts[i].replace("&nbsp;", " ").strip()
        if "    &tmp;" in temp:
            temp = temp.replace("    &tmp;", separator)
        else:
            temp = temp.replace("&tmp;", "")
        parts[i] = _autoparse_to_data_type(temp, allow_boolean, NaN)
    return parts

def _autoparse_to_data_type(string, allow_boolean, NaN):
    """ Decode DSV strings into equivalent Python data types. """
    formatted = string.strip()
    if len(formatted):
        if formatted == "null":
            return None
        if formatted == "NaN":
            return NaN
        if allow_boolean:
            if formatted.lower() in ("yes", "y"):
                return True
            if formatted.lower() in ("no", "n"):
                return False
        try:
            numeric = float(formatted)
            if not (numeric-(numeric//1)):
                return int(numeric)
            return numeric
        except:
            pass
    return formatted

def _write_file(data):
    """ Save formatted DSV into file. """
    if not (isinstance(data._filepath, str) and isinstance(data._encoding, str)):
        return
        
    packed = data._packed
    if not isinstance(packed, str):
        packed = _pack(data)

    try:
        with open(data._filepath, "w+", encoding=data._encoding) as f:
            f.write(packed)
    except:
        print("MaguroWarning: Unable to update selected file.")

def _read_file(data):
    """ Read DSV file and attempt to create a list object. """
    if not (isinstance(data._filepath, str) and isinstance(data._encoding, str)):
        return
    if not isinstance(data._delimiter, str):
        return
    sep1 = data._delimiter
    sep2 = None
    if isinstance(data._newline, str):
        sep1 = data._newline
        sep2 = data._delimiter

    temp = []
    allow_boolean = isinstance(data._allow_boolean, bool) and bool(data._allow_boolean)
    try:
        with open(data._filepath, "r", encoding=data._encoding) as f:
            values = f.read().split(sep1)
            for value in values:
                if len(value:=value.strip()):
                    if sep2 is not None:
                        temp.append(_clean_split(value, sep2, allow_boolean, data._NaN))
                        continue
                    temp.append(_autoparse_to_data_type(value, allow_boolean, data._NaN))
    except:
        pass
    return temp