#!/usr/bin/python3

"""Define class for a singly linked list."""


class Node:
    """Represent a node."""

    def __init__(self, data, next_node=None):
        """Initialization of a new node.

        Args:
            data (int).Node value
            nextNode (Node). Next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the value of Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class to represent a singly linked list."""

    def __init__(self):
        """Initalize Singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the Singly Linked List.

        Args:
            value (Node). The new node value.
        """

        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            newNode.next_node = temp.next_node
            temp.next_node = newNode

    def __str__(self):
        """Define the print function rep of a Singly Linked List."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
