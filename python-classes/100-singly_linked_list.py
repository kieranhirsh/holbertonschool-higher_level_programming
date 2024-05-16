#!/usr/bin/python3
''' module documentation. is empty for now '''


class Node:
    ''' this class defines a node of a singly linked list

    Args:
        data (int): the data stored at this node
        next_node (Node): the next node

    Attributes (int):
        data (int): the data stored at this node
        next_node (Node): the next node'''
    def __init__(self, data, next_node=None):
        """
        Method to initialize a node

        Args:
            data (int): the data stored at this node
            next_node (Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data stored at this node

        Returns:
            (int): the data stored at this node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data stored at thsi node

        Args:
            (int): the data stored at this node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next node

        Returns:
            (Node): the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next node

        Args:
            (Node): the next node
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    ''' this class defines a singly linked list

    Args:
        None

    Attributes (int):
        head (Node): the head node'''
    def __init__(self):
        """
        Method to initialize a singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        Method to define the print() behaviour of this class
        """
        ptr = self.__head

        if ptr is None:
            return ""
        else:
            while ptr.next_node is not None:
                print(ptr.data)
                ptr = ptr.next_node

        print(ptr.data, end="")
        return ""

    def sorted_insert(self, value):
        """
        Method to add a node to this singly linked list

        Args:
            value (int): the value stored at this node
        """
        ptr = self.__head

        if ptr is None:
            self.__head = Node(value)
        elif value <= ptr.data:
            new_node = Node(value, ptr)
            self.__head = new_node
        else:
            while ptr.next_node is not None and ptr.next_node.data < value:
                ptr = ptr.next_node
            new_node = Node(value, ptr.next_node)
            ptr.next_node = new_node
