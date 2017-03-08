"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        counter = 1
        while counter < position:
          if current.next:
            current = current.next
            counter += 1
          else: 
            return None
          
        return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        previous = None
        current = self.head
        while counter < position:
          if current:
            previous = current
            current = current.next
            counter += 1
          else:
            pass

        if counter == position:
          new_element.next = current
          previous.next = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        previous = None
        current = self.head
        if current.value == value:
          self.head = current.next 
        else:
          while current.next:
            previous = current
            current = current.next
            if current.value == value:
              previous.next = current.next
              

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print("should be 3:")
print(ll.head.next.next.value)
# Should also print 3
print("should be 3:")
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print("should be 4:")
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print("should be 2:")
print(ll.get_position(1).value)
# Should print 4 now
print("should be 4:")
print(ll.get_position(2).value)
# Should print 3 now
print("should be 3:")
print(ll.get_position(3).value)
