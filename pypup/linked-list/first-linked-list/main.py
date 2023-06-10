class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def first_linked_list():
    return LinkedList(314)


print(first_linked_list())
