Back to [Welcome](welcome.md)

#

# The Binary Search Tree

## Introduction

The Binary Search Tree (BST) is a data structure that is useful for times when you want efficiency in adding, removing, and checking if a value is a member, but you do not want to use a [set](set.md).

[![I add a 6](6_bst.png)](https://www.youtube.com/watch?v=UNY4uqCnYqs)

**Above**, I add a 6 to the tree. It is **the root**.

[![I add a 5](5_bst.png)](https://www.youtube.com/watch?v=UNY4uqCnYqs)

**Above**, I add a 5 to the tree. It is placed on the **left** of the 6, because 5 is **less than** 6.

[![I add an 8](8_bst.png)](https://www.youtube.com/watch?v=UNY4uqCnYqs)

**Above**, I add an 8 to the tree. It is placed on the **right** of the 6, because 8 is **greater than** 6.

[![I add a 9](9_bst.png)](https://www.youtube.com/watch?v=UNY4uqCnYqs)

**Above**, I add a 9 to the tree. It is placed on the **right** of the 6 and the **right** of the 8, because 9 is **greater than** 6 and **greater than** 8.

[![More is added](end_bst.png)](https://www.youtube.com/watch?v=UNY4uqCnYqs)

**Above**, more is added to the tree. Can you see why the new cards were placed in their spots? See the video below for the answers.

Here is the full video explaining a bit about the BST: [Binary Search Tree Demonstration](https://www.youtube.com/watch?v=UNY4uqCnYqs)

### Balance

Some of the operations of a BST can be of performance: O(log n). However if that tree is not balanced, it can reach O(n). For example, if we drew the above cards in this order:
* 2
* 5
* 6
* 7
* 8
* 9
* 10

This would lead to the the BST looking like a diagonal line of cards connected together. If a computer wanted to find the **10** in this setup, it would have to go through **all** the other cards to find it (not very efficient). With the above setup, however, it would have to go through the **6**, then the **8**, and then the **9**. After those, it would reach the **10**.

## Methods and Performance

There are a number of methods associated with the BST. Here are **some** of the methods, what they do, and their Big O performance:

| Method | What it does | Big O Performance |
| - | - | - |
| insert | inserts a new item into the BST | O(log n)* |
| remove | removes an item from the BST | O(log n)* |
| member | checks if a value is in the BST | O(log n)* |
| traverse forward | go to all the items, in an ascending order | O(n) |
| traverse backward | go to all the items, in an descending order | O(n) |
| size | checks the size of the bst | O(1) |
| empty | checks if the size is  | O(1) |

*It can be O(log n) if the tree is balanced

## Python Implementation

In order to use a BST Python, we need to use custom class. Please view and study the methods of this custom BST class file: [BinarySearchTree.py](BinarySearchTree.py). This is the BST class we will be using for this tutorial. Let's say we instantiated a new BST:
```
my_bst = BinarySearchTree()
```
Using `my_bst` here is how we would implement the **some** of the above mentioned methods:

| Method | Implementation |
| - | - |
| insert | `my_bst.insert(value_to_insert)` |
| member | `my_bst.member(value_to_check)` |
| traverse forward | `for i in my_bst.forward():` |
| traverse backward | `for i in my_bst.backward():` |
| size | `my_bst.size` |
| empty | `my_bst.root == None` |

## Some Possible Problems

### Only storing numbers in the BinarySearchTree

You may realize that with the custom [BinarySearchTree](BinarySearchTree.py) class, we are only able to store numbers in the tree. 

If you wanted to stored other values, you might consider an approach like the one [bintrees](https://pypi.org/project/bintrees/) uses. They store key+value couples in the tree.

Another approach to this problem could be to have a separate Python dictionary that holds the number stored in the BST as a **key** and the true value as the **value**. For example
```
tree = BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree_dict = {1:"A", 2:"B", 3:"C"}
```

### Not using the forward and backward methods correctly

You may find that trying to traverse a [BinarySearchTree](BinarySearchTree.py) does not work as you might expect when you do something like this:
```
# print the contents of my_bst in ascending order
print(my_bst.forward())
```
It is good to know that the forward and backward methods give values to a `for` loop. For example:
```
# print the contents of my_bst in ascending order
for i in my_bst.forward():
    print(i)
```
## Tree Example

### Scenario

Here is a shuffled list of numbers from 0-99:
```
numbers = [18, 79, 55, 94, 47, 15, 22, 51, 44, 93, 82, 52, 78, 85, 26, 74, 6, 16, 70, 87, 2, 58, 39, 14, 36, 27, 42, 90, 0, 7, 1, 9, 56, 20, 30, 17, 91, 29, 45, 75, 69, 11, 59, 25, 31, 23, 68, 95, 72, 99, 12, 10, 84, 98, 46, 3, 33, 76, 66, 54, 19, 77, 61, 37, 43, 89, 80, 8, 38, 13, 96, 65, 73, 4, 5, 28, 97, 40, 21, 62, 32, 92, 41, 67, 88, 24, 81, 60, 71, 53, 64, 57, 35, 50, 48, 63, 49, 34, 83, 86]
```
How might a BST be used to sort these numbers?

### Solution

Let us add the numbers into a BST and then traverse the BST, adding them into a new `sorted_numbers` list.
```
# import BinarySearchTree to be used
from BinarySearchTree import BinarySearchTree

# create the numbers list to be sorted
numbers = [18, 79, 55, 94, 47, 15, 22, 51, 44, 93, 82, 52, 78, 85, 26, 74, 6, 16, 70, 87, 2, 58, 39, 14, 36, 27, 42, 90, 0, 7, 1, 9, 56, 20, 30, 17, 91, 29, 45, 75, 69, 11, 59, 25, 31, 23, 68, 95, 72, 99, 12, 10, 84, 98, 46, 3, 33, 76, 66, 54, 19, 77, 61, 37, 43, 89, 80, 8, 38, 13, 96, 65, 73, 4, 5, 28, 97, 40, 21, 62, 32, 92, 41, 67, 88, 24, 81, 60, 71, 53, 64, 57, 35, 50, 48, 63, 49, 34, 83, 86]

# create the BST
bst = BinarySearchTree()

# insert the values of numbers into bst
for i in numbers:
    bst.insert(i)

# create a new sorted_numbers list
sorted_numbers = list()

# traverse bst forward and add the values to sorted_numbers
for i in bst.forward():
    sorted_numbers.append(i)

# display sorted_numbers to the user
print(sorted_numbers)
```
Here is the output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```
## Practice Problem

### Scenario

Let's say we are running a business with different employees. Our business is currently using [employee_data.csv](employee_data.csv) to keep track of employee information. We keep track of the employee `id`, `name`, and `salary`:
```
id,name,salary
0,Steve,34.33
1,Maxine,45.33
2,Jim,345.55
...
```
We would like to transfer our employee information to a BST. **Your tasks are to:**
1. Modify the [BinarySearchTree](BinarySearchTree.py) class so that there is capability for keeping track of employees (their `id`, `name`, and `salary`), ordered by the `id`
2. Add a method called `find` to return the `name` and `salary` (in a tuple) of an employee according to the given id (return tuple: `(None, None)` if there is no such `id`)
3. Add the employee data from [employee_data.csv](employee_data.csv) to this new BST
4. Using the `find` method, determine the `name` and `salary` of employee#: **909** and display a message saying:
```
$<salary> payed to <name> 
```

### Solution

When you are ready, view my [solution](tree_solution.py) with the output in a comment at the top.

#

Back to [Welcome](welcome.md)