from abc import ABCMeta, abstractmethod


class Node:
    def __init__(self, element, prev_node=None, next_node=None):
        self._element = element
        self._prev_node = prev_node
        self._next_node = next_node

    def getElement(self):
        return self._element

    def getPrev(self):
        return self._prev_node

    def getNext(self):
        return self._next_node

    def setElement(self, item):
        self._element = item

    def setPrev(self, item):
        self._prev_node = item

    def setNext(self, item):
        self._next_node = item

    def toString(self):
        return 'Node: Element', self._element, '|Next Node Element',\
               self._next_node, '|Previous Node Element', self._prev_node


class List(object):
    __metaclass__ = ABCMeta

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __len__(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.getNext()
        return counter

    def __iter__(self):
        current = self.head
        while current is not None:
            current = current.getNext()

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if item is current.getElement():
                return True
            else:
                current = current.getNext()
        return False

    def __getitem__(self, item):
        current = self.head
        while current is not None:
            if item is current.getElement():
                return current
            else:
                current = current.getNext()
        print("Error: Node with value", item, "is not in the Linked List.")

    def __str__(self):
        counter = 0
        current = self.head
        while current is not None:
            print("Node at position", counter, "contains value", current.getElement(),
                    "has previous", current.getPrev(), "and next", current.getNext())
            current = current.getNext()
            counter += 1

    @abstractmethod
    def __setitem__(self, index, newItem):
        pass

    @abstractmethod
    def insert(self, elem, index):
        pass

    @abstractmethod
    def append(self, elem):
        pass

    def appendAll(self, elems):
        for i in elems:
            self.append(i)

    @abstractmethod
    def push(self, elem):
        pass


class LinkedList(List):

    def __init__(self, head=None, tail=None):
        super(self.__class__, self).__init__(head, tail)

    def __setitem__(self, index, newItem):
        counter = 0
        current = self.head
        while current is not None:
            if counter == index:
                current.setElement(newItem)
                break
            else:
                current = current.getNext()
                counter += 1
        print("Node at index", index, "has been given value", newItem)

    def insert(self, elem, index):
        if index == 0:  # Base Case
            self.push(elem)

        else:
            counter = 0
            current = self.head
            while counter < index-1:
                current = current.getNext()
                counter += 1

            tmp = Node(elem,None,current.getNext())
            current.setNext(tmp)

            if current is self.tail:
                self.tail = tmp

        print("Value", elem, "has been inserted into the list at position", index)

    def append(self, elem):
        tmp = Node(elem)
        self.tail.setNext(tmp)
        self.tail = tmp

    def push(self, elem):
        if self.head is not None and self.head.getNext() is None:
            self.tail = self.head
        tmp = Node(elem, None, self.head)
        self.head = tmp

    def pushAll(self, elems):
        for i in elems:
            self.push(i)

    def reverse(self):
        if self.__len__() < 2:
            print("List is too short to be reversed.")
        temp = LinkedList()
        current = self.head
        while current is not None:
            temp.push(current.getElement())
            current = current.getNext()
        return temp  # Note: Set the list or return a copy? - chose not to modify original (INTENTIONAL)


class DoubleLinkedList(List):

    def __init__(self, head=None, tail=None):
        super(self.__class__, self).__init__(head, tail)

    def __setitem__(self, index, newItem):
        current = self.head
        counter = 0
        while current is not None:
            if counter == index:
                current = Node(newItem, current.getPrev(), current.getNext())
            counter += 1
            current = current.getNext()

    def insert(self, elem, index):
        if index == 0:
            self.push(elem)
        else:
            counter = 0
            current = self.head
            while counter < index - 1:
                current = current.getNext()
                counter += 1

            tmp = Node(elem, current, current.getNext())
            current.getNext().setPrev(tmp)
            current.setNext(tmp)

    def append(self, elem):
        if self.__len__() < 2:
            if self.__len__() == 1:
                tmp = Node(elem, self.head, None)
                self.tail = tmp
                self.head.setNext(tmp)
            else:
                self.head = Node(elem)
        else:
            tmp = Node(elem, self.tail, None)
            self.tail.setNext(tmp)
            self.tail = tmp

    def push(self, elem):
        tmp = Node(elem, None, self.head)
        if self.__len__() < 2:
            if self.__len__() == 0:
                self.head = tmp
            else:
                self.tail = self.head
                self.head = tmp
                self.tail.setPrev(self.head)
        else:
            self.head.setPrev(tmp)
            self.head = tmp

    def reverse(self):
        if self.__len__() < 2:
            print("List is too small to be reversed")
        else:
            start = self.head
            end = self.tail
            for i in range(0, (self.__len__()//2)):
                tmp = start.getElement()    # Simple 3-line swap
                start.setElement(end.getElement())
                end.setElement(tmp)

                start = start.getNext()
                end = end.getPrev()

s = DoubleLinkedList()  # Test __init__
s.append(7)  # Test append()
s.push(1)  # Test push()
s.append(2)
s.insert(8, 1)  # Test insert()
s.append(6)
s.append(4)
s.__setitem__(3, 15)  # Test __setitem__
s.__str__()  # Test return
print("It is", s.__contains__(6), "that the list contains this value")
print("It is", s.__contains__(123), "that the list contains this value")  # Test __contains__
s.reverse()  # Test reverse
print("\n")
s.__str__()  # Prove reverse

l = LinkedList()
l.append(7)  # Test append()
l.push(1)  # Test push()
l.append(2)
l.insert(8, 1)  # Test insert()
l.append(6)
l.append(4)
l.__setitem__(3, 15)  # Test __setitem__
l.__str__()  # Test return
print("It is", s.__contains__(6), "that the list contains this value")
print("It is", s.__contains__(123), "that the list contains this value")  # Test __contains__
l.reverse()  # Test reverse
print("\n")
l.__str__()  # Prove reverse
