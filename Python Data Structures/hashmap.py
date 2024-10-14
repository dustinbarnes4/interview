"""Name: Dustin Barnes
Class: 2420-001
Project 7: Dictionaries
All of the following code was written by me. This implements a
hashmap dictionary."""

class Word():
    """Specific to this HashMaps use, this object
    named Word is a data type with a key and value
    that is a data item within the hashmap."""
    def __init__(self, key, value=1):
        """Initializes the key and value of a new Word."""
        self.key = key
        self.value = value

    def increment(self):
        """Used for word count, allows the HashMap to
        increment the wordcount by one when the same word
        is entered into the HashMap."""
        self.value += 1

    def __str__(self):
        """Returns a string in the form of a tuple for the
        key and value of the word object."""
        return "(" + self.key +", " + str(self.value) + ")"

class HashMap():
    """HashMap data structure."""
    def __init__(self):
        """Initializes HashMap with 8 slots and a size of 0."""
        self.hash_table = [None] * 8
        self.hash_size = 0

    def hash_function(self, key):
        """Hash's a string to find index for hash_table"""
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % self.capacity()

    def get(self, key, default=None):
        """Returns the value of a key if it is in the HashMap,
        if it is not, it will return None."""
        index = self.hash_function(key)
        if self.hash_table[index] is None: #pylint: disable=R1705
            return default
        elif self.hash_table[index].key == key:
            return self.hash_table[index].value
        else:
            original_index = index
            while self.hash_table[index] is not None:
                if self.hash_table[index].key == key:
                    return self.hash_table[index].value
                index = (index + 1) % self.capacity()
                if index == original_index:
                    break
            return default

    def set(self, key, value=1):
        """Puts a key and value into the Hashmap, if the value is not
        provided it defaults at one. Also checks to see if the key is
        already in the HashMap and if it is it will increment its value
        by one unless a new value is given by the user."""
        if self.get(key) is None:
            index = self.hash_function(key)
            if self.hash_table[index] is None:
                self.hash_table[index] = Word(key, value)
                self.hash_size += 1
            else:
                while self.hash_table[index] is not None:
                    index = (index + 1) % self.capacity()
                self.hash_table[index] = Word(key, value)
                self.hash_size += 1
        else:
            index = self.hash_function(key)
            while True:
                if self.hash_table[index].key == key:
                    if value != 1:
                        self.hash_table[index].value = value
                    else:
                        self.hash_table[index].increment()
                    break
                index = (index + 1) % self.capacity()
        if self.size()/self.capacity() >= 0.8:
            self.rehash()

    def clear(self):
        """Resets the HashMap with 8 slots."""
        self.hash_table = [None] * 8
        self.hash_size = 0

    def capacity(self):
        """Returns the total number of buckets
        in the HashMap."""
        return len(self.hash_table)

    def size(self):
        """Returns the number of filled buckets."""
        return self.hash_size

    def keys(self):
        """Returns a list of Keys in the HashMap."""
        keys_list = []
        for item in self.hash_table:
            if item is not None:
                keys_list.append(item.key)
        return keys_list

    def values(self):
        """Returns a list of Values in the HashMap."""
        values_list = []
        for item in self.hash_table:
            if item is not None:
                values_list.append(item.value)
        return values_list

    def sort_by_value(self):
        """Returns a sorted list of (key, value) tuples
        that are sorted by the value."""
        keys_values_list = []
        for item in self.hash_table:
            if item is not None:
                keys_values_list.append((item.key, item.value))
        sorted_list = sorted(keys_values_list, key=lambda x: x[1], reverse=True)
        return sorted_list

    def rehash(self):
        """Rehashes the HashTable by doubling its size
        and then replacing all of the items into their new
        spot that has been recalculated."""
        old_table = self.hash_table
        self.hash_size = 0
        self.hash_table = [None] * (2 * self.capacity())
        for item in old_table:
            if item is not None:
                self.set(item.key, item.value)
