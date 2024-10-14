"""Name: Dustin Barnes
Course: 2420-001
Project: 6 Balanced Trees
File: binarysearchtree.py
All of the following code was written by me."""
from recursioncounter import RecursionCounter

class Node():
    """Node class, holds data for the nodes of the bst."""
    def __init__(self, data, left_child=None, right_child=None):
        """Constructor of the Node class, sets data, children,
        and node height."""
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        """Returns true or false based on whether or not the
        node is a leaf. This is determined through seeing if
        the node height is equal to 0."""
        if self.height == 0:
            return True
        return False

    def update_height(self):
        """Updates the height of the node when called."""
        if self.left_child is None:
            left = -1
        else:
            left = self.left_child.height
        if self.right_child is None:
            right = -1
        else:
            right = self.right_child.height
        self.height = max(left, right) + 1

    def __str__(self):
        """Creates the string value of the node including
        the data and height of the node."""
        output = str(self.data) + " " + "(" + str(self.height) + ")"
        if self.is_leaf():
            output = output + " [leaf]"
        return output

class BinarySearchTree():
    """Core binary search tree (bst) data structure."""
    def __init__(self):
        """constructor for the bst, sets root to None."""
        self.root = None

    def is_empty(self):
        """Returns bool value for whether or not the bst is empty."""
        if self.root is None:
            return True
        return False

    def add(self, data): #pylint: disable=R1710
        """Add metod for bst enabling the ability to add
        nodes to the tree. Uses an embedded helper function
        to help facilitate adding recursively."""
        def add_helper(cursor, data): #pylint: disable=R1710
            """Recursive helper method that recurses through the tree
            to find the properly sorted location for a new node."""
            RecursionCounter()
            if data == cursor.data:
                return
            if data < cursor.data:
                if cursor.left_child is None: #pylint: disable=R1705
                    cursor.left_child = Node(data)
                    return cursor.update_height()
                else:
                    return add_helper(cursor.left_child, data), cursor.update_height()
            if data > cursor.data:
                if cursor.right_child is None: #pylint:disable=R1705
                    cursor.right_child = Node(data)
                    return cursor.update_height()
                else:
                    return add_helper(cursor.right_child, data), cursor.update_height()

        if self.root is None:
            self.root = Node(data)
        else:
            return add_helper(self.root, data)

    def find(self, data):
        """Find method that finds and returns desired node. Uses
        helper method to facilitate this recursively."""
        def find_helper(cursor, data):
            """Helper method that recurses through the tree to find
            the desired node. Uses the nodes data to accomplish this and
            returns the first occurance of the given data."""
            RecursionCounter()
            if cursor is None: #pylint: disable=R1705
                return None
            elif data == cursor.data:
                return cursor
            elif data < cursor.data:
                return find_helper(cursor.left_child, data)
            else:
                return find_helper(cursor.right_child, data)

        return find_helper(self.root, data)

    def remove(self, data): #pylint: disable=R0915
        """Removes the first occurance of the given data. Uses a helper
        to recurse through the tree."""
        def remove_helper(cursor, data):
            """Helper function that recurses through the tree and removes
            the first node with the given data. Handles many different
            situations for locations of nodes."""
            RecursionCounter()
            if cursor is not None:
                #Left and right variables to reduce the characters of code in logic comparisons.
                #These variables are only used in if statements. Variable assignment within
                #if statments need to use "cursor.left_child" etc.. so that proper assignment
                #happens within the trees.
                left = cursor.left_child
                right = cursor.right_child
                #First case: item is not in the tree.
                if self.find(data) is None:
                    raise ValueError("the item is not in the tree")
                #Second case: item to be removed is the root.
                if self.root.data == data:
                    if self.root.left_child is None and self.root.right_child is None:
                        #Root to be deleted is the only node in the tree.
                        self.root = None
                    elif self.root.left_child is not None and self.root.right_child is None:
                        #Root to be deleted has only left child.
                        self.root = self.root.left_child
                    elif self.root.left_child is None and self.root.right_child is not None:
                        #Root to be deleted has only right child.
                        self.root = self.root.right_child
                    elif self.root.left_child is not None and self.root.right_child is not None:
                        #Root to be deleted has two children.
                        parent, successor = self.find_minimum(self.root.right_child)
                        if self.root.right_child.left_child is None:
                            #Checks to see if root.right is the left most node in the right subtree.
                            #If it is, then it takes root's place.
                            self.root.data = self.root.right_child.data
                            self.root.right_child = self.root.right_child.right_child
                        else:
                            #Searches for the successor, the left most node in the right subtree
                            #and replaces root with that data value.
                            self.root.data = successor.data
                            if successor is parent.right_child:
                                parent.right_child = successor.right_child
                            if successor is parent.left_child:
                                parent.left_child = successor.right_child
                    if self.root is None: #pylint: disable=R1705
                        return
                    else:
                        return self.root.update_height()
                elif left is not None and left.data == data and left.is_leaf():
                    #Node to be deleted is cursor.left_child and it is a leaf.
                    cursor.left_child = None
                    return cursor.update_height()
                elif right is not None and right.data == data and right.is_leaf():
                    #Node to be deleted is cursor.right_child and it is a leaf.
                    cursor.right_child = None
                    return cursor.update_height()
                elif left is not None and left.data == data and left.left_child is not None and left.right_child is None: #pylint: disable=C0301
                    #Node to be deleted is cursor.left_child and has only left child.
                    cursor.left_child = cursor.left_child.left_child
                    return cursor.update_height()
                elif left is not None and left.data == data and left.right_child is not None and left.left_child is None: #pylint: disable=C0301
                    #Node to be deleted is cursor.left_child and has only right child.
                    cursor.left_child = cursor.left_child.right_child
                    return cursor.update_height()
                elif right is not None and right.data == data and right.left_child is not None and right.right_child is None: #pylint: disable=C0301
                    #Node to be deleted is cursor.right_child and has only left child.
                    cursor.right_child = cursor.right_child.left_child
                    return cursor.update_height()
                elif right is not None and right.data == data and right.right_child is not None and right.left_child is None: #pylint: disable=C0301
                    #Node to be deleted is cursor.right_child and has only right child.
                    cursor.right_child = cursor.right_child.right_child
                    return cursor.update_height()
                elif left is not None and left.data == data and left.left_child is not None and left.right_child is not None: #pylint: disable=C0301
                    #Node to be deleted is cursor.left_child and it has two children.
                    if left.right_child.left_child is None:
                        #If cursor.left_child's right child is the left most in the right subtree
                        #then it replaces cursor.left_child.
                        cursor.left_child.data = cursor.left_child.right_child.data
                        cursor.left_child.right_child = cursor.left_child.right_child.right_child
                    else:
                        #Finds the successor node, being the left most node in the right subtree
                        #of cursor.left_child and relocates it to cursor.left_child's position.
                        #"Deletes" cursor.left_child by moving successors data into left_child's
                        #data field and then removes the successor and makes necessary shift
                        #depending on if the successor was a right or left child.
                        parent, successor = self.find_minimum(cursor.left_child.right_child)
                        cursor.left_child.data = successor.data
                        if successor is parent.right_child:
                            parent.right_child = successor.right_child
                        if successor is parent.left_child:
                            parent.left_child = successor.right_child
                    return cursor.update_height()
                elif right is not None and right.data == data and right.left_child is not None and right.right_child is not None: #pylint: disable=C0301
                    #Node to be deleted is cursor.left_child and it has two children.
                    if right.right_child.left_child is None:
                        #If cursor.right_child's right child is the left most in the right subtree
                        #then it replaces cursor.left_child.
                        cursor.right_child.data = cursor.right_child.right_child.data
                        cursor.right_child.right_child = cursor.right_child.right_child.right_child
                    else:
                        #Finds the successor node, being the left most node in the right subtree
                        #of cursor.right_child and relocates it to cursor.right_child's position.
                        #"Deletes" cursor.right_child by moving successors data into right_child's
                        #data field and then removes the successor and makes necessary shift
                        #depending on if the successor was a right or left child.
                        parent, successor = self.find_minimum(cursor.right_child.right_child)
                        cursor.right_child.data = successor.data
                        if successor is parent.right_child:
                            parent.right_child = successor.right_child
                        if successor is parent.left_child:
                            parent.left_child = successor.right_child
                    return cursor.update_height()

                else:
                    #If item was not found on this pass, recurse through the tree.
                    if data < cursor.data:
                        return remove_helper(cursor.left_child, data), cursor.update_height()
                    if data >= cursor.data:
                        return remove_helper(cursor.right_child, data), cursor.update_height()

        return remove_helper(self.root, data)

    def find_minimum(self, cursor=None):
        """Uses a loop to find the left most node in a given tree
        or subtree. Returns the left most node as well as that nodes
        parent node."""
        if cursor is None:
            if self.root is None: #pylint: disable=R1720
                raise ValueError("the tree is empty")
            else:
                cursor = self.root
        parent = None
        node = cursor
        while node.left_child is not None:
            parent = node
            node = node.left_child
        return parent, node

    def find_maximum(self, cursor=None):
        """Uses a loop to find the right-most value in a given tree
        or subtree."""
        if cursor is None:
            if self.root is None: #pylint:disable=R1720
                raise ValueError("the tree is empty")
            else:
                cursor = self.root
        node = cursor
        while node.right_child is not None:
            node = node.right_child
        return node

    def rebalance_tree(self):
        """Rebalances the bst. Uses a recursive helper
        function to do this."""
        def rebalance_tree_helper(lyst):
            """Recursively rebalances the tree by making the
            middle value the new root and then adding nodes
            by dividing the lyst into two parts and adding in the
            middle node of each one."""
            RecursionCounter()
            mid_point = len(lyst)//2
            left_high = mid_point
            right_low = mid_point + 1
            if len(lyst) != 0:
                self.add(lyst[mid_point])
            if left_high < 0:
                left_high = 0
            if left_high > 0:
                rebalance_tree_helper(lyst[0:left_high])
            if len(lyst) != 0 and right_low < len(lyst):
                rebalance_tree_helper(lyst[right_low:len(lyst)])

        inorder_lyst = list(self.inorder())
        self.root = None
        rebalance_tree_helper(inorder_lyst)

    def inorder(self):
        """In order traversal of the tree. Uses
        a helper function to do this recursively."""
        def inorder_helper(cursor, lyst):
            """Recursive function that generates an in order
            iterator of the tree. In order by integer value."""
            RecursionCounter()
            if cursor is not None:
                inorder_helper(cursor.left_child, lyst)
                lyst.append(cursor.data)
                inorder_helper(cursor.right_child, lyst)

        inorder_lyst = []
        cursor = self.root
        inorder_helper(cursor, inorder_lyst)
        return iter(inorder_lyst)

    def preorder(self):
        """Creates and returns a preorder list
        of nodes in the tree. Uses a helper function to accomplish this."""
        def preorder_helper(cursor, output):
            """Helper function that recurses through the list and adds
            the data of each node to a list that is returned. The data is added
            in preorder."""
            RecursionCounter()
            if cursor is not None:
                output.append(cursor.data)
                preorder_helper(cursor.left_child, output)
                preorder_helper(cursor.right_child, output)

        preorder_lyst = []
        cursor = self.root
        preorder_helper(cursor, preorder_lyst)
        return iter(preorder_lyst)

    def height(self):
        """Returns the height of the tree, which is
        equal to the height of the root. If there is no
        nodes in the tree it returns -1."""
        if self.root is None: #pylint: disable=R1705
            return -1
        else:
            return self.root.height

    def __str__(self):
        """Method for string representation of the tree.
        Uses a helper method to accomplish this."""
        def str_helper(cursor, output, tab_level=0): #pylint: disable=R1710
            """Helper function that recursively builds
            a string representation of the tree. Includes
            the data, height, and indicates if its a leaf.
            If a node is not a leaf and has an empty child
            spot it will output empty in the tree string.
            Indents each level of the tree according to its
            level and the number of levels above it."""
            RecursionCounter()
            if cursor is not None:
                output.append("    " * tab_level)
                tab_level = tab_level + 1
                output.append(str(cursor) + "\n")
                if cursor.is_leaf(): #pylint: disable=R1705
                    return output
                else:
                    str_helper(cursor.left_child, output, tab_level)
                    str_helper(cursor.right_child, output, tab_level)
                    return output
            if cursor is None:
                output.append("    " * tab_level)
                tab_level = tab_level + 1
                output.append("[Empty]\n")
                return output
        output = []
        final_output = ""
        cursor = self.root
        str_helper(cursor, output)
        for item in output:
            final_output = final_output + item
        return final_output

    def __len__(self):
        """Length function that returns an integer
        for the number of nodes in the tree. Uses a
        helper node to accomplish this."""
        def len_helper(cursor, counter):
            """Length helper node. Recursively builds a list
            of the items in the tree and then returns an integer
            for the number of nodes in the tree."""
            RecursionCounter()
            if cursor is not None:
                counter.append(cursor.data)
                len_helper(cursor.left_child, counter)
                len_helper(cursor.right_child, counter)

        counter = []
        cursor = self.root
        len_helper(cursor, counter)
        return len(counter)
        