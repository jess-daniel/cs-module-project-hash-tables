class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.new_list = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        # Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash_value = offset_basis
        for char in key:
            hash_value = hash_value * FNV_prime
            hash_value = hash_value ^ ord(char)
        return hash_value

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hashed_idx = self.hash_index(key)

        if not self.new_list[hashed_idx]:
            self.new_list[hashed_idx] = HashTableEntry(key, value)
            self.size += 1
        # something is already at the index
        else:
            current = self.new_list[hashed_idx]
            # iterate and replace item's value
            while current.key != key and current.next:
                current = current.next

            if current.key == key:
                current.value = value
            # nothing found, add a new item
            else:
                current.next = HashTableEntry(key, value)
                self.size += 1

        # handle resizing
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.new_list[self.hash_index(key)] = None
        hashed_idx = self.hash_index(key)
        current = self.new_list[hashed_idx]

        if not current:
            print(f"Error: There is no key {key}")
        elif not current.next:
            self.new_list[hashed_idx] = None
            self.size -= 1
        else:
            # create a pointer for the current item's previous item
            previous = None
            while current.key != key and current.next:
                previous, current = current, current.next
            # if the current item is at the end of the list
            if not current.next:
                previous.next = None
                self.size -= 1
            # current item is in the middle of the list
            else:
                previous.next = current.next
                self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.new_list[(self.hash_index(key))]

        hashed_idx = self.hash_index(key)
        current = self.new_list[hashed_idx]
        # if index, return its value
        if current:
            return current.value
        # otherwise, return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_table = HashTable(new_capacity)

        for item in self.new_list:
            current = item
            while current:
                new_table.put(current.key, current.value)
                current = current.next
        # overwrite table with new data
        self.capacity = new_table.capacity
        self.size = new_table.size
        self.new_list = new_table.new_list


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
