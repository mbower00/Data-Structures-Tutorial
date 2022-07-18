#OUTPUT:28.88 payed to Jonathan

class EmployeeBinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
    
    class Node:
        """Nodes have a emp_id, name, and salary and the capability of holding a 
        left and a right Node
        """
        def __init__(self, emp_id, name, salary):
            self.emp_id = emp_id
            self.name = name
            self.salary = salary
            self.left = None
            self.right = None
    
    def insert(self, emp_id, name, salary):
        # update the size
        self.size += 1
        # if this is the first node in the tree, add it to the root
        if self.root == None:
            self.root = self.Node(emp_id, name, salary,)
        # else, call the recursive insert function to insert the node at the right spot
        else:
            self._recursive_insert(emp_id, name, salary, self.root)
    
    def _recursive_insert(self, emp_id, name, salary, root : Node):
        if root.emp_id > emp_id:
            # if the emp_id belongs on the left
            if root.left == None:        
                # add node to the left
                root.left = self.Node(emp_id, name, salary)
            else:
                self._recursive_insert(emp_id, name, salary, root.left)
        else:
            if root.right == None:
                # add node to the right
                root.right = self.Node(emp_id, name, salary)
            else:
                self._recursive_insert(emp_id, name, salary, root.right)
    
    def find(self, emp_id):
        # call the recursive find function with the root
        return self._recursive_find(emp_id, self.root)

    def _recursive_find(self, emp_id, root):
        # if the root is None, we have exhausted the search, so return None
        if root == None:
            return (None, None)
        # if the root emp_id is the emp_id, we have found the emp_id, so return name and salary
        elif root.emp_id == emp_id:
            return (root.name, root.salary)
        # if the emp_id belongs on the left
        elif root.emp_id > emp_id:
            # call function again with the left of the root
            return self._recursive_find(emp_id, root.left)
        else:
            # call function again with the right of the root
            return self._recursive_find(emp_id, root.right)

    def member(self, emp_id):
        # call the recursive member function with the root
        return self._recursive_member(emp_id, self.root)

    def _recursive_member(self, emp_id, root):
        # if the root is None, we have exhausted the search, so return False
        if root == None:
            return False
        # if the root emp_id is the emp_id, we have found the emp_id, so return True
        elif root.emp_id == emp_id:
            return True
        # if the emp_id belongs on the left
        elif root.emp_id > emp_id:
            # call function again with the left of the root
            return self._recursive_member(emp_id, root.left)
        else:
            # call function again with the right of the root
            return self._recursive_member(emp_id, root.right)

    def forward(self):
        # call the recursive forward function for the root of the tree
        yield from self._recursive_forward(self.root)

    def _recursive_forward(self, root):
        if root != None: # If the root is an actual Node...
            # call the recursive forward function for the left side of the root to be yielded
            yield from self._recursive_forward(root.left)
            # yield the root
            yield root.emp_id
            # call the recursive forward function for the right side of the root to be yielded
            yield from self._recursive_forward(root.right)

    def backward(self):
        # call the recursive backward function for the root of the tree
        yield from self._recursive_backward(self.root)

    def _recursive_backward(self, root):
        if root != None: # If the root is an actual Node...
            # call the recursive backward function for the right side of the root to be yielded
            yield from self._recursive_backward(root.right)
            # yield the root
            yield root.emp_id
            # call the recursive backward function for the left side of the root to be yielded
            yield from self._recursive_backward(root.left)

def main():
    # create the EmployeeBinarySearchTree
    emp_bst = EmployeeBinarySearchTree()

    with open("employee_data.csv") as f:
        is_first = True
        for i in f:
            # skip the first line
            if is_first:
                is_first = False
                continue
            # clean i
            i = i.strip()
            # split i by "," into emp_info
            emp_info = i.split(",")
            # make the id an integer
            emp_info[0] = int(emp_info[0])
            # make the salary a float
            emp_info[2] = float(emp_info[2])
            # add info to emp_bst
            emp_bst.insert(emp_info[0], emp_info[1], emp_info[2])

    # get the name and salary (as a tuple) of employee#: 909
    emp_909 = emp_bst.find(909)

    # display $<salary> payed to <name>
    print(f"{emp_909[1]} payed to {emp_909[0]}")
        

if __name__ == "__main__":
    main()