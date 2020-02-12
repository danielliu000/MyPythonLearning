from Singly_Linked_List import SinglyLinkedList


class Node(object):
    ''' '''

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(SinglyLinkedList):

    def add_first(self, data):
        ''' add a new node to a linked list from the head/root '''

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        new_node.next.prev = new_node

        return new_node.data

    def add_append(self, data):
        ''' add a new node to a linked list from the last --- append a node '''

        new_node = Node(data)
        cur = self.head

        if cur == None:
            self.head = new_node

        else:
            while cur.next != None:
                cur = cur.next

            new_node.prev = cur
            cur.next = new_node

        return new_node.data

    def insert_node(self, index, data):
        ''' insert a node from the middle of a linked list '''

        if index <= 0 or self.head is None:
            self.add_first(data)
        elif index >= self.get_size():
            self.add_append(data)

        else:

            new_node = Node(data)
            cur = self.head
            pos = 1

            while pos < index:

                pos += 1
                cur = cur.next

            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

    def find_node(self, data):
        ''' check if a node data in a linked list '''

        return True if data in self.traversal() else False

    def remove_data(self, data):
        ''' remove a node from a linked list based on its data '''

        if self.is_empty():
            return 'list is null, removal failed'
        if not self.find_node(data):
            return 'no data found, removal failed'

        cur = self.head

        if cur.data == data:
            self.head = cur.next
            if cur.next:
                cur.next.prev = None
                return 'data removed'
        else:
            while cur.data != data:
                cur = cur.next

            if cur.next is None:
                cur.prev.next = None
                cur.prev = None

            else:
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
            return 'data removed'

    def remove_index(self, index):
        ''' remove a node from a linked list based on a given index '''

        if self.is_empty():
            return 'list is null, removal failed'
        if index < 0 or index >= self.get_size():
            return 'index out of range, removal failed'

        cur = self.head

        count = 0

        if index == 0:
            self.head = cur.next
            if cur.next:
                cur.next.prev = None
                return 'data removed'
        else:
            while count != index:
                count += 1
                cur = cur.next

            if cur.next is None:
                cur.prev.next = None
                cur.prev = None

            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            return 'data removed'


if __name__ == '__main__':

    l1 = DoublyLinkedList()
    l1.add_append(1)
    '''
    l1.add_append(2)
    l1.add_append(4)
    l1.insert_node(2, 3)
    l1.insert_node(4, 6)
    '''
    l1.remove_data(1)
    print(l1.traversal())
