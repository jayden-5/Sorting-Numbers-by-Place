import random

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

def main():
    var = 0
    item_list = []
    num_place = []
    max_range = int(input("Enter Max Range: "))
    list_size = int(input("Enter list size: "))
    digits_of_max_range = len(str(max_range))
    for i in range(10):
        num_place.append(Queue())
    for i in range(list_size):
        theRange = random.randrange(max_range)
        item_list.append(theRange)
    print('''
'''f"Radix Pass 0: {item_list} ")
    for i in range(digits_of_max_range):
        for num in item_list:
            number = num // 10**i % 10
            num_place[number].enqueue(num)
        item_list = []
        for q in num_place:
            while not q.is_empty():
                item_list.append(q.dequeue())
        var += 1
        print("Radix Pass", var, ":", item_list)

main()


#Works cited:
#https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python


'''Enter max range: 99999
   Enter list size: 10'''

'''Enter max range: 9999999999
   Enter list size: 6'''