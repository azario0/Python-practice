"""
A multiset is the same as set except that an element might occur more than once in a multiset, 
Implement a multiset data structure in Python. Implement 4 methods
"""
class Multiset:
    def __init__(self): # initializes the multiset with an empty dict
        self.elements = {}
        
    def add(self, val): # adds an element to the multiset. if the element exists. its counts is incremented
        self.elements[val] = self.elements.get(val, 0) + 1
        
    def remove(self, val): # removes an element from the  multiset. if the element counter > 1, its count is decremented. if the element's count become 0, it is removed from the multiset.
        if val in self.elements:
            self.elements[val] -= 1
            if self.elements[val] == 0:
                del self.elements[val]
                
    def __contains__(self, val):# checks if an element is in the multiset by check if it is in the dict
        return val in self.elements
    
    def __len__(self): """ returns the number of elements in the multiset by summing up the counts of all elements in the dict"""
        return sum(self.elements.values())
    
if __name__ == '__main__': """
create a new multiset , add two elements to it, add a duplicate element, remove one occurrence of the duplicate element, and then print out whethr 2 and 3are in multiset and the number of elements in the multiset."""
    mset = Multiset()
    print(mset.add(int(input())))
    print(mset.add(int(input())))
    mset.add(int(input()))
    mset.remove(int(input()))
    print(2 in mset)
    print(3 in mset)
    print(len(mset))


