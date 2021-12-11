from main import Pair

class Node():
    def __init__(self, data, left_child=None, right_child=None):
        self.new_pair = Pair(data)
        self.left_child = left_child
        self.right_child = right_child


class BST():
    def __init__(self):
        self.root is None
        self.counter = 0


    def is_empty(self):
        if self.root is None:
            return True

    def size(self):
        return self.counter


    def add(self, data):
        """
        :param data:
        :return:
        """
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
        else:
            self.add_helper(self.root, data)
        self.counter += 1


    def add_helper(self, cursor, data):
        """
        :param cursor:
        :param data:
        :return:
        """
        if data >= cursor.data:
            if cursor.right_child is None:
                cursor.right_child = Node(data)
            else:
                self.add_helper(cursor.right_child, data)
        else:
            if cursor.left_child is None:
                cursor.left_child = Node(data)
            else:
                self.add_helper(cursor.left_child, data)


    
        
