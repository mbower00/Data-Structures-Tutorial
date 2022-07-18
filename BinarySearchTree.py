class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
    
    class Node:
        """Nodes have a value and the capability of holding a 
        left and a right Node
        """
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def insert(self, value):
        # update the size
        self.size += 1
        # if this is the first node in the tree, add it to the root
        if self.root == None:
            self.root = self.Node(value)
        # else, call the recursive insert function to insert the node at the right spot
        else:
            self._recursive_insert(value, self.root)
    
    def _recursive_insert(self, value, root : Node):
        if root.value > value:
            # if the value belongs on the left
            if root.left == None:        
                # add node to the left
                root.left = self.Node(value)
            else:
                self._recursive_insert(value, root.left)
        else:
            if root.right == None:
                # add node to the right
                root.right = self.Node(value)
            else:
                self._recursive_insert(value, root.right)
    
    def member(self, value):
        # call the recursive member function with the root
        return self._recursive_member(value, self.root)

    def _recursive_member(self, value, root):
        # if the root is None, we have exhausted the search, so return False
        if root == None:
            return False
        # if the root value is the value, we have found the value, so return True
        elif root.value == value:
            return True
        # if the value belongs on the left
        elif root.value > value:
            # call function again with the left of the root
            return self._recursive_member(value, root.left)
        else:
            # call function again with the right of the root
            return self._recursive_member(value, root.right)

    def forward(self):
        # call the recursive forward function for the root of the tree
        yield from self._recursive_forward(self.root)

    def _recursive_forward(self, root):
        if root != None: # If the root is an actual Node...
            # call the recursive forward function for the left side of the root to be yielded
            yield from  self._recursive_forward(root.left)
            # yield the root
            yield root.value
            # call the recursive forward function for the right side of the root to be yielded
            yield from  self._recursive_forward(root.right)

    def backward(self):
        # call the recursive backward function for the root of the tree
        yield from self._recursive_backward(self.root)

    def _recursive_backward(self, root):
        if root != None: # If the root is an actual Node...
            # call the recursive backward function for the right side of the root to be yielded
            yield from  self._recursive_backward(root.right)
            # yield the root
            yield root.value
            # call the recursive backward function for the left side of the root to be yielded
            yield from  self._recursive_backward(root.left)