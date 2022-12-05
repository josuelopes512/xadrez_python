# Design HashSet in python
# checking the values and will return the output class
class Checkingvalues:
    # initialization function which has list mathfun
    def __init__(self):
        self.mathfun = {}

    # update vales function
    # def update(self, key):
    #     found = False
    #     for i, k in enumerate(self.mathfun):
    #         if key == k:
    #             self.mathfun[i] = key
    #             found = True
    #             break
    #     if not found:
    #         self.mathfun.append(key)
    
    def update(self, key):
        if isinstance(key, object):
            found = False
            for k, _ in self.mathfun.items():
                if key.hash == k:
                    self.mathfun[k] = key
                    found = True
                    break
            if not found:
                self.mathfun[key.hash] = key
        else:
            found = False
            for k, _ in self.mathfun.items():
                if key == k:
                    self.mathfun[k] = key
                    found = True
                    break
            if not found:
                self.mathfun[key] = key

    # get values function
    def get(self, key):
        for k in self.mathfun.keys():
            if k == key:
                return True
        return False
    # remove values function

    def remove(self, key):
        for k in self.mathfun.keys():
            if key == k:
                del self.mathfun[k]

# class HashSet main class


class HashSet:
    # Initialization function
    def __init__(self):
        self.key_space = 2096
        self.hash_table = [Checkingvalues() for i in range(self.key_space)]

    def hash_values(self, key):
        hash_key = key % self.key_space
        return hash_key
    # add function

    def add(self, key):
        if isinstance(key, object):
            if key.hash:
                self.hash_table[self.hash_values(key.hash)].update(key)
        else:
            self.hash_table[self.hash_values(key)].update(key)
    # remove function

    def remove(self, key):
        self.hash_table[self.hash_values(key)].remove(key)
    # contains function

    def contains(self, key):
        return self.hash_table[self.hash_values(key)].get(key)

    def display(self):
        ls = []
        for i in self.hash_table:
            if len(i.mathfun) != 0:
                ls.append(i.mathfun[0])
        print(ls)

    def toList(self):
        ls = []
        for i in self.hash_table:
            if i.mathfun:
                ls.append(i.mathfun.keys())
        return ls

    def difference(self, x, y):
        return list(set(x) - set(y))

    def union(self, x, y):
        return list(set(x) | set(y))
    
    def intersection(self, x, y):
        return list(set(x) & set(y))
    
    def ExceptWith(self, hashList):
        a = self.toList()
        b = hashList.toList()
        
        for key in self.difference(self.union(a, b), self.difference(a, b)):
            if self.contains(key):
                self.remove(key)
