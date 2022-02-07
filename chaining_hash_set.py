from chaining_hash_node import ChainingHashNode
class ChainingHashSet():
    def __init__(self, capacity=0):
        self.hash_table = [None] * capacity
        self.table_size = 0
        self.capacity = capacity

    def get_hash_code(self, key):
        """Hash function that calculates a hash code for a given key using the modulo division.
        :param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        :return:
        		The calculated hash code for the given key.
        """
        return key % self.capacity

    def get_hash_table(self):
        """(Required for testing only)
        :return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table):
        """(Required for testing only) Set a given hash table..
        :param table: Given hash table which shall be used.

        !!!
        Since this method is needed for testing we decided to implement it.
        You do not need to change or add anything.
        !!!

        """
        self.hash_table = table
        self.capacity = len(table)
        self.table_size = 0
        for node in table:
            while node is not None:
                self.table_size += 1
                node = node.next

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!)."""
        counter = 0
        for i in self.hash_table:
            if i is not None:
                curr_node = i
                while curr_node is not None:
                    curr_node = curr_node.next
                    counter +=1
        self.table_size = counter
        return counter

    def insert(self, key):
        """Inserts a key and returns True if it was successful. If there is already an entry with the
          same key, the new key will not be inserted and False is returned.
         :param key:
         		The key which shall be stored in the hash table.
         :return:
         		True if key could be inserted, or False if the key is already in the hash table.
         :raises:
         		a ValueError if any of the input parameters is None.
         """
        if key is None:
            raise ValueError

        if self.contains(key) is True:
            return False

        self._insert(key)
        return True



    def _insert(self,key):
        hash_code =  self.get_hash_code(key)

        if self.hash_table[hash_code] is None: #handle the case where we don't have an entry
            self.hash_table[hash_code] = ChainingHashNode(key)
        elif self.hash_table[hash_code] is not None: #handle the case where we already have an entry on that position e.g. chaining
            curr_node = self.hash_table[hash_code]
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = ChainingHashNode(key)

    def contains(self, key):
        """Searches for a given key in the hash table.
         :param key:
         	    The key to be searched in the hash table.
         :return:
         	    True if the key is already stored, otherwise False.
         :raises:
         	    a ValueError if the key is None.
         """
        if key == None:
            raise ValueError

        hash_code = self.get_hash_code(key)

        if self.hash_table[hash_code] is None:
            return False

        elif self.hash_table[hash_code] is not None:
            if self.hash_table[hash_code].next is None:
                if self.hash_table[hash_code].key == key:
                    return True
            else:
                curr_node = self.hash_table[hash_code]
                while curr_node is not None:
                    if curr_node.key == key:
                        return True
                    else:
                        curr_node = curr_node.next
        return False



    def remove(self, key):
        """Removes the key from the hash table and returns True on success, False otherwise.
        :param key:
        		The key to be removed from the hash table.
        :return:
        		True if the key was found and removed, False otherwise.
        :raises:
         	a ValueError if the key is None.
        """

        if key is None:
            raise ValueError
        if self.contains(key) is False:
            return False

        self._remove(key)
        return True

    def _remove(self, key):
        hash_code = self.get_hash_code(key)

        if self.hash_table[hash_code] is None:
            return False
        if self.hash_table[hash_code] is not None: #handle the case where we have an entry on the hash_code position
            if self.hash_table[hash_code].next is None: #handle the case when the entry is the first node in chaining
                self.hash_table[hash_code] = None
            elif self.hash_table[hash_code].next is not None: #handle the case where the entry is not the first node in chaining
                curr_node = self.hash_table[hash_code]
                if self.hash_table[hash_code].key == key:
                    self.hash_table[hash_code] = self.hash_table[hash_code].next
                else:
                    while curr_node.next.key != key:
                        curr_node = curr_node.next
                    if curr_node.next.next is None:
                        curr_node.next.next = None
                        curr_node.next.key = None
                        curr_node.next = None
                    elif curr_node.next.next is not None:
                        curr_node.next = curr_node.next.next
    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        self.hash_table = [None] * self.capacity
        self.capacity = 0

    def to_string(self):
        """Returns a string representation of the hash table (array indices and stored keys) in the format
            Idx_0 {Node, Node, ... }, Idx_1 {...}
            e.g.: 0 {13}, 1 {82, 92, 12}, 2 {2, 32}, """
        big_list = []
        for i, node in enumerate(self.hash_table):
            list_of_nodes = []
            while node is not None:
                list_of_nodes.append(node.key)
                node = node.next
            big_list.append([i,list_of_nodes])
        string = ""
        for term in big_list:
            string += str(term[0]) + " {"
            if term[1] == []:
                string += 'None}, '
            else:
                for i in term[1]:
                    string += str(i)+", "
                string = string[:-2]
                string +="}, "
        string = string[:-2]
        print(string)

