# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of slots in the hash table
        # pre-allocate an array with a definite size
        self.storage = [None] * capacity
        self.count = 0  # number of actual items stored in the hash table

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # using Python's built in hash function returns a hashed value
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # pass the key to our _hash method
        # modulus by the length of our capacity to return an index that fits
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        if self.capacity == self.count - 1:
            self.resize()

        # first hash the key to get an index value
        index = self._hash_mod(key)

        # now create a new linkedPair node to hold the key, value data
        new_node = LinkedPair(key, value)

        # if that index location is available,
        if self.storage[index] is None:
            # store the new_node at the indexed position in storage
            self.storage[index] = new_node
            self.count += 1
        else:  # if that index location is already taken
            # store the linked pair node already there into a temp variable
            temp = self.storage[index]
            if temp.key == key:  # if the new key is the same
                # then simply update the value
                self.storage[index].value = value
                return None
            else:  # if the new key is not the same as the key already there -> collision
                while temp.next is not None:  # loop thru link nodes until key is found
                    temp = temp.next
                    if temp.key == key:  # checking each item in the linked list to see if the key is already stored
                        temp.value = value  # if the key is already stored, update with the new value
                        return None
            temp.next = new_node  # once at the end of the linked list, add the new LinkedPair
            self.count += 1  # increment count of items in the hash table

        return None

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Prints a warning if the key is not found.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]  # retrieve what is at that index

        if current is None:
            print(f'Warning! {key} is not in the hash table')
            return None
        else:
            # if a value is there, store it in a temp variable
            temp = self.storage[index]

            if temp.next != None:
                if temp.next.key == key:  # check for a match
                    temp.next = temp.next.next  # reassign
                    self.count -= 1
                temp = temp.next
            else:
                if temp.key == key:
                    self.storage[index] = None
                    return None

            return None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:  # if the value is found
            # get the linked list or value stored at that index into a variable
            temp = self.storage[index]

            while temp != None:  # loop through the linked list
                if temp.key == key:  # compare each key
                    return temp.value  # if found, return the value
                temp = temp.next  # go to next item in linked list

        return None  # else not found

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
