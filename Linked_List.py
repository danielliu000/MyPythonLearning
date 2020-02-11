class Node(object):

    ''' define a node for linked ist'''

    def __init__(self, data, next_data=None):

        self.data = data
        self.next = None

    def get_node(self):

        return self.data

    def get_next(self):

        return self.next

    def set_node(self, data):

        self.data = data

    def set_next(self, data):

        self.next = data


class LinkedList(object):

    ''' define a linked list '''

    def __init__(self, head=None):

        self.head = head
        self.size = 0

    def is_empty(self):

        return self.head is None

    def get_size(self):

        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def travel(self):

        cur = self.head
        result = []

        while cur is not None:

            result.append(cur.data)
            cur = cur.next
        return result

    def add_first(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        return new_node.data

    def add_append(self, data):

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

        return True if data in self.travel() else False

    def remove_data(self, data):

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


if __name__ == "__main__":

    l1 = LinkedList()

    print(l1.is_empty())

    print(l1.add_first(1))
    print(l1.add_append(3))
    print(l1.add_append(5))
    print(l1.add_append(7))
    print(l1.travel())
    print(l1.remove_index(6))

    print(l1.travel())
