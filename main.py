"""Generates a tree and calculates its characteristics"""

from tree import generate_random_tree, get_tree_info

if __name__ == "__main__":
    print("\nTo generate random tree, enter the number of the tree nodes >> ...")
    number_of_nodes = int(input())
    print(get_tree_info(generate_random_tree(number_of_nodes)))
