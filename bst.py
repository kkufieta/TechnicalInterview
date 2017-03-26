class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_node(self.root, new_val)

    def insert_node(self, start, new_val):
        if start:
          if new_val < start.value:
            if start.left:
              self.insert_node(start.left, new_val)
            else:
              start.left = Node(new_val)
          else:
            if start.right:
              self.insert_node(start.right, new_val)
            else:
              start.right = Node(new_val)
              
        else:
          start = Node(new_val)
          

    def search(self, find_val):
        return self.search_node(self.root, find_val)

    def search_node(self, start, find_val):
        if start and find_val == start.value:
          return True
        if start.left and find_val < start.value:
          return self.search_node(start.left, find_val)
        if start.right and find_val >= start.value:
          return self.search_node(start.right, find_val)
        
        return False

    def print_tree(self):
        return self.print_post_order(self.root, "")[:-1]

    def print_post_order(self, start, traversal):
        if start.left:
          traversal = self.print_post_order(start.left, traversal)
        if start.right:
          traversal = self.print_post_order(start.right, traversal)
        if start:
          traversal += str(start.value) + "-"
        return traversal
      
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
