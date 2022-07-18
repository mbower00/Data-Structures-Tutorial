# Here, I abstracted the earlier explained Python implementation of the queue data structure into a
# class called MyQueue. It has the methods of a queue as mentioned in queue.md
class MyQueue:
    # create a queue member variable that is a dynamic array
    def __init__(self):
        self.queue = []

    # define the method to add a value to the back of the queue
    def enqueue(self, value):
        self.queue.append(value)

    # define the method the take and return a value from the front of the queue
    def dequeue(self):
        return self.queue.pop(0)
    
    # define the method to return the size of the queue
    def size(self):
        return len(self.queue)
    
    # define the method to return whether or not the queue is empty
    def empty(self):
        return len(self.queue) == 0

# create the queue for the evens
even_q = MyQueue()
# create the queue for the odds
odd_q = MyQueue()

# open the O.txt file
with open("O.txt") as f:
        # loop through the file
        for i in f:
            if i.count("O") % 2 == 0: # if O count is even
                # add it to the even queue
                even_q.enqueue(i)

            else:
                # add it to the odd queue
                odd_q.enqueue(i)

# start a new file called O_separate.txt
with open("O_separate.txt", "x") as f_separate:
        # loop through a range with the size of the odd queue
        for _ in range(odd_q.size()):
            # print the dequeued value from the odd queue
            print(odd_q.dequeue(), end="", file=f_separate)

        # loop through a range with the size of the even queue
        for _ in range(even_q.size()):
            # print the dequeued value from the even queue
            print(even_q.dequeue(), end="", file=f_separate)