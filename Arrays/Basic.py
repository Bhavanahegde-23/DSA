#Arrays
# capacity() - number of items it can hold
# prepend(item) - can use insert above at index 0
# resize(new_capacity) // private function
# when you reach capacity, resize to double the size
# when popping an item, if the size is 1/4 of capacity, resize to half
#check all delete , remove method

class Arrays:
    def __init__(self):
        self.arr = []

    # size() - number of items -- > works
    def size(self):
        count =0
        for i in self.arr:
            count += 1
        return count

    # is_empty()
    def is_empty(self):
        return self.arr == []

    # at(index) - returns the item at a given index, blows up if index out of bounds
    def at(self , index):
        for i in range(len(self.arr)):
            if i == index:
                return self.arr[i]
        return -1

    # push(item)
    def push(self , item):
        self.arr.append(item)
        return self.arr

    # insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    def insert(self,index,item):
        for i in range(len(self.arr)):
            if i == index:
                self.arr[i] = item
        return self.arr

    #Need to understand this
    # pop() - remove from end, return value
    def pop(self):
        if self.size() == 0:
            raise IndexError("List is empty")

        value = self.arr[self.size() - 1]
        # self.size -= 1   # just decrease logical size
        return value

    # delete(index) - delete item at index, shifting all trailing elements left -- something wrong
    def delete(self, index=None):
        if self.size == 0:
            raise IndexError("List empty")

        if index is None:
            index = self.size() - 1

        if index < 0 or index >= self.size():
                raise IndexError("Index out of range")

        value = self.arr[index]

        # shift elements left
        for i in range(index, self.size() - 1):
            self.arr[i] = self.arr[i + 1]

        return self.arr

    # remove(item) - looks for value and removes index holding it (even if in multiple places)
    def remove(self,item):
        for i in range(self.size()):
            if self.arr[i] == item:
                self.delete(i)
        return self.arr

    # find(item) - looks for value and returns first index with that value, -1 if not found
    def find(self,item):
        for i in range(self.size()):
            if item == self.arr[i]:
                return i,item

        return -1,item


a = Arrays()
a.arr = [2,2,2,4,5]
print(a.find(2))









