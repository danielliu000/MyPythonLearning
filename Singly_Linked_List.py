class Node(object):

    ''' define a node for linked ist'''

    def __init__(self, data, next_data=None):
        ''' define and initialize a node elements '''

        self.data = data
        self.next = None

    def get_node(self):
        ''' get a node value '''

        return self.data

    def get_next(self):
        ''' get next value of a node '''

        return self.next

    def set_node(self, data):
        ''' give a value for a node '''

        self.data = data

    def set_next(self, data):
        ''' give a value of next node '''

        self.next = data


class SinglyLinkedList(object):

    ''' define a linked list '''

    def __init__(self, head=None):
        ''' define a linked list elements '''

        self.head = head

    def is_empty(self):
        ''' check if the linked list is null '''

        return self.head is None

    def get_size(self):
        ''' get the length/size of a linked list '''

        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def traversal(self):
        ''' traverse the whole linked list, return a list of values '''

        cur = self.head
        result = []

        while cur is not None:

            result.append(cur.data)
            cur = cur.next
        return result

    def add_first(self, data):
        ''' add a new node to a linked list from the head/root '''

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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
            cur.next = new_node

    def find_node(self, data):
        ''' check if a node value in a linked list '''

        return True if data in self.travel() else False

    def remove_data(self, data):
        ''' remove a node from a linked list based on its value '''

        if self.is_empty():
            return 'list is null, removal failed'
        if not self.find_node(data):
            return 'no data found, removal failed'

        cur = self.head
        pre = None

        if cur.data == data:
            self.head = cur.next
            return 'data removed'
        else:
            while cur.data != data:
                pre = cur
                cur = cur.next
            pre.next = cur.next
            return 'data removed'

    def remove_index(self, index):
        ''' remove a node from a linked list based on a given index '''

        if self.is_empty():
            return 'list is null, removal failed'
        if index < 0 or index >= self.get_size():
            return 'index out of range, removal failed'

        cur = self.head
        pre = None
        count = 0

        if index == 0:
            self.head = cur.next
            return 'data removed'
        else:
            while count != index:
                count += 1
                pre = cur
                cur = cur.next

            pre.next = cur.next
            return 'data removed'

    def reverse_linked_list(self):
        ''' reverse a linked list '''

        if self.is_empty():
            return 'the linked list is null, reverse failed'
        else:
            reversed_list = self.traversal()
            reversed_list.reverse()
            return reversed_list


def merge_linked_list(l1, l2):

    if l1.is_empty() and not l2.is_empty():
        return l2.traversal()
    elif l2.is_empty() and not l1.is_empty():
        return l1.traversal()
    else:

        list_1 = l1.traversal()
        list_2 = l2.traversal()

        merged_list = [*list_1, *list_2]
        merged_list.sort()

        return merged_list


if __name__ == "__main__":

    l1 = SinglyLinkedList()
    '''
    l1.add_first(1)
    l1.add_append(3)
    l1.add_append(5)
    l1.add_append(7)
    '''
    l2 = SinglyLinkedList()
    '''
    l2.add_first(1)
    l2.add_append(2)
    l2.add_append(3)
    l2.add_append(4)
    '''
    print(l1.traversal())
    print(l2.traversal())

    print(l1.reverse_linked_list())
    print(merge_linked_list(l1, l2))
