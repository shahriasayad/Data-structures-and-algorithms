class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(4)
head.next = Node(6)
head.next.next = Node(23)
head.next.next.next = Node(88)
head.next.next.next.next = Node(99)
head.next.next.next.next.next = Node(149)
head.next.next.next.next.next.next = Node(264)
head.next.next.next.next.next.next.next = Node(397)
head.next.next.next.next.next.next.next.next = Node(471)


def print_list(head_value):

    if head_value is None:
        return
    else:
        present_node = head_value
        while present_node is not  None:
            print(present_node.data)
            present_node = present_node.next

print_list(head)

