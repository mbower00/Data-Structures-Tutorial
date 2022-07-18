# The Set

Back to [Welcome](welcome.md)

## Introduction

The set is a powerful data structure that can be useful if you want **good efficiency for adding, removing, and determining us a value is contained in the list** and you do not care about order or saving duplicates. A set **does not allow repeated values**. This can be a blessing and a curse. A set also **does not keep track of the order** of the items contained within.

When you **add** something to a set, you will (if there are no conflicts):
1. Take a **hash** of the value you would like to add
2. Get the **hash modulo the number of indexes**
3. Place the value **at that index** (found in step 2)

[!["JOKER"](joker.png)](https://www.youtube.com/watch?v=YKdW0XQRxIU)

Here, I have the the string "JOKER", which I want to be add to my set.

[!["JOKER" hash](joker_hash.png)](https://www.youtube.com/watch?v=YKdW0XQRxIU)

I took the **hash** of "JOKER" and got this value.

[![hash modulo the number of indexes (14)](equation.png)](https://www.youtube.com/watch?v=YKdW0XQRxIU)

I did **hash modulo the number of indexes (14)**.

[![equals four](equals_four.png)](https://www.youtube.com/watch?v=YKdW0XQRxIU)

I got **4**.

[!["JOKER" added to index 4](joker_added.png)](https://www.youtube.com/watch?v=YKdW0XQRxIU)

I **added** "JOKER" to **index 4**.

Here is the full video explaining a bit about the set: [Set Demonstration](https://www.youtube.com/watch?v=YKdW0XQRxIU).

### Conflicts

It may happen that the system mentioned above will want to place multiple different values in the **same index**. This is called a **conflict**. For example: What if we then drew a 4? The above mentioned system would want to place that 4 in index 4, however "JOKER" is already at index 4.

A couple ways of dealing with conflicts are **open addressing** (placing the value first open spot to the right of the conflict) and **chaining** (adding a list to the conflicted index and adding the conflicted to the list). By resolving a conflict in these ways, we can end up making our performance worse than O(1).

## Methods and Performance

There are a number of methods associated with the Set. Here are the methods, what they do, and their Big O performance:

| Method | What it does | Big O Performance |
| - | - | - |
| add | adds a value to the set | O(1)* |
| remove | removes a value from the set | O(1)* |
| member | checks if a value is in the set | O(1)* |
| size | checks the size of the set | O(1) |

*This can be made worse than O(1) if there are conflicts

## Python Implementation

To create a set in Python we can follow this pattern:
```
my_set = set()
```
Here is a solution to implement the above methods in Python for set: `my_set`.

| Method | Python |
| - | - |
| add | `my_set.add(my_value_to_add)` |
| remove | `my_set.remove(my_value_to_remove)` |
| member | `my_value_to_check in my_set` |
| size | `len(my_set)` |

## Some Possible Errors

### Losing track of duplicates

You might try do add a value that is identical to a value that is already in the set. Take a look at this example from the shell:
```
>>> s = set()
>>> s.add(1)
>>> s
{1} 
>>> s.add(1)
>>> s
{1} 
```
Notice how I did not get a warning saying that I was adding a value (1, in this case) that is already in the set. This could potentially lead to a loss of data if I needed to keep track of that 1.

A way to guard against this is to check if the value we are adding is already a member. For example:
```
duplicates = []
if value in my_set:
    duplicates.append(value)
    print(f"{value} already in set. {value} added to duplicates")
else:
    my_set.add(value)
```
Here, if `value` is already in `my_set`, we add the duplicate value to a list called `duplicates` and print out a message. If `value` is not a duplicate, we add it to `my_set`.

### Losing track of order

You might add items to a set and they will not necessarily be placed in the set in the order in which they were received. Here is an example from the shell:
```
>>> my_set = set() 
>>> my_set.add(500)
>>> my_set.add(20)  
>>> my_set.add(600)
>>> my_set.add("cat")
>>> my_set           
{600, 500, 20, 'cat'}
```
As you can see, the values added to the set do not always appear in the order in which they were added.

If you need to keep track of the order in which you added items, you could create a separate list that holds the values in the proper order (NOTE: you may want not want to add duplicates to the list, because they will not be in the set). Here is an example from the shell:
```
>>> my_set = set()
>>> my_list = list()
>>> my_set.add("Max")
>>> my_list.append("Max")
>>> my_set.add("Eddie")   
>>> my_list.append("Eddie")
>>> my_set.add("Nancy")     
>>> my_list.append("Nancy") 
>>> my_set                  
{'Eddie', 'Max', 'Nancy'}
>>> my_list                
['Max', 'Eddie', 'Nancy']
```
As you can see, the `my_list` is in the order in which the strings were added, while `my_set` is not. You could use a list to find out the order, and use a set for membership test (which could be a better Big O performance). A drawback to this strategy is that it will take up more space than just having a list or a set.

## Set Example

### Scenario

Let's say there is an zoo that charges people for day passes. When someone visits the zoo, they will be charged for that day. If they leave and come back in the same day, they would still need to give their name at the gate upon reentry. The zoo has been getting number of complaints from people claiming that they **got charged two times** for the same day!

Here is the gate's log of admissions for a day (stored in list `gate_log`):
```
gate_log = ["Maxine", "Jim", "Billy", "Billy", "Maxine", "Joyce", "Mike", "Nancy", "El", "Jonathan", "Dustin"]
```
How might a **set** be used so that Billy and Maxine do **not** get charged two times for one day?

### Solution
Lets add the 
```
# store the gate log in a list
gate_log = ["Maxine", "Jim", "Billy", "Billy", "Maxine", "Joyce", "Mike", "Nancy", "El", "Jonathan", "Dustin"]

# create a set and pass in the gate log
gate_set = set(gate_log)

# loop through the set
for i in gate_set:
    # display that the person has been charged
    print(f"{i:10} Charged")
```
Here is the output:
```
Maxine     Charged
Jim        Charged
Jonathan   Charged
El         Charged
Billy      Charged
Nancy      Charged
Dustin     Charged
Mike       Charged
Joyce      Charged
```
Notice that Billy and Maxine were not charged twice.

## Practice Problem

### Scenario

Continuing on with the example of the Zoo, let us suppose that the zoo will now charge **$10** as an entry fee. The zoo will also charge a small amount of **$5** to anyone upon reentry to the zoo. If they enter again (for a third time that day) they will be charged **$2**. Any further entries that day will be **free**.

Use this gate's log of admissions for a day (stored in list `gate_log`):
```
gate_log = ["Maxine", "Jim", "Billy", "Billy", "Maxine", "Mike", "El", "Dustin", "Billy", "Maxine", "Joyce", "Billy", "Maxine", "Joyce", "Mike", "Nancy", "El", "Jonathan", "Dustin", "Steve", "Joyce"]
```

**Use sets to implement this new zoo policy.**

The people should be charged according to this example output:
```
FIRST ENTRY CHARGES
El         Charged $10
Jim        Charged $10
Billy      Charged $10
Nancy      Charged $10
Dustin     Charged $10
Joyce      Charged $10
Jonathan   Charged $10
Maxine     Charged $10
Steve      Charged $10
Mike       Charged $10

SECOND ENTRY CHARGES
El         Charged $5
Billy      Charged $5
Dustin     Charged $5
Joyce      Charged $5
Maxine     Charged $5
Mike       Charged $5

THIRD ENTRY CHARGES
Joyce      Charged $2
Billy      Charged $2
Maxine     Charged $2
```

### Solution

When you are ready, view my [solution](set_solution.py)