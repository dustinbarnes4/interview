"""Name: Dustin Barnes
Course: 2420-001
Project: 5 Trees
File: binarysearchtree.py
All of the following code was written by me."""
from binarysearchtree import BinarySearchTree

def main():
    """Main function, prints representation of a tree
    created by the main function. It then removes nodes
    and prints the new tree."""
    tree = BinarySearchTree()
    nodes = [21, 9, 4, 2, 3, 7, 14, 10, 18, 15, 26, 30, 28]
    for item in nodes:
        tree.add(item)
    preorder_list = tree.preorder()
    preorder_string = ""
    for item in preorder_list:
        preorder_string = preorder_string + str(item) + ", "
    print(preorder_string)
    print(tree)
    node_delete = [21, 9, 4, 18, 15, 7]
    for item in node_delete:
        tree.remove(item)
    print(tree)

if __name__ == "__main__":
    main()
