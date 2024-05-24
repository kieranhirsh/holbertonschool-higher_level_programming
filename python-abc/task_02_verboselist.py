#!/usr/bin/python3
''' module documentation '''


class VerboseList(list):
    ''' this class defines a verbose list, it inherits from the in-built python
    list '''
    def append(self, item):
        """
        method to append an item to the list

        Args:
            item: the item to append
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        method to extend a list

        Args:
            items (list): the items to append to the list
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """
        method to remove an item from the list

        Args:
            item: the item to remove
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, idx=None):
        """
        method to pop an item from the list

        Args:
            idx (int): the index to pop
        """
        if idx is None:
            idx = len(self) - 1
        print("Removed [{}] from the list.".format(self[idx]))
        super().pop(idx)

