# Class Definition (hashtable)
class hashtable:
    def __init__(self):  # Constructor of the hashtable class                                    
        self.m = int(input("Enter size of hash table: "))     
        self.hashTable = [None] * self.m  # Initializes the hash table
        self.elecount = 0                                    
        self.comparisons = 0  # Number of comparisons made during insertion/searching
        print(self.hashTable)  # Prints the initial empty hash table

    # Hash Function
    def hashFunction(self, key):
        return key % self.m

    # Check if Hash Table is Full
    def isfull(self):
        return self.elecount == self.m

    # Linear Probing Insert Method
    def linearprobr(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        while self.hashTable[index] is not None:
            index = (index + 1) % self.m  # Wrap around
            compare += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"No. of comparisons: {compare}")

    # Linear Probing Search Method
    def getlinear(self, key, data):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            index = (index + 1) % self.m
        return None

    # Quadratic Probing Insert Method
    def quadraticprobr(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 0
        while self.hashTable[index] is not None:
            index = (index + i * i) % self.m  # Quadratic probing
            compare += 1
            i += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"No. of comparisons: {compare}")

    # Quadratic Probing Search Method
    def getQuadratic(self, key, data):
        index = self.hashFunction(key)
        i = 0
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index
            i += 1
            index = (index + i * i) % self.m
        return None    

    # Insert Using Linear Probing
    def insertvialinear(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:
            print("Collision occurred, applying Linear Probing")
            self.linearprobr(key, data)

    # Insert Using Quadratic Probing
    def insertviaQuadratic(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:
            self.hashTable[index] = [key, data]
            self.elecount += 1
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:
            print("Collision occurred, applying Quadratic Probing")
            self.quadraticprobr(key, data)

# Menu Function
def menu():
    obj = hashtable()
    
    ch = 0
    while ch != 3:
        print("************************")
        print("1. Linear Probe")
        print("2. Quadratic Probe")
        print("3. Exit")
        print("************************")

        ch = int(input("Enter Choice: "))
        
        if ch == 1:
            ch2 = 0
            while ch2 != 3:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj.insertvialinear(a, b)
                elif ch2 == 2:
                    k = int(input("Enter key to be searched: "))
                    b = str(input("Enter name: "))
                    f = obj.getlinear(k, b)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")
        elif ch == 2:
            ch2 = 0
            obj1 = hashtable()
            while ch2 != 3:
                print("** 1. Insert **")
                print("** 2. Search **")
                print("** 3. Exit **")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj1.insertviaQuadratic(a, b)
                elif ch2 == 2:
                    k = int(input("Enter key to be searched: "))
                    b = str(input("Enter name: "))
                    f = obj1.getQuadratic(k, b)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")

menu()
