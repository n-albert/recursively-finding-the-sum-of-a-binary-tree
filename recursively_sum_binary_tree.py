class BinaryTreeNode:
    def __init__(self, input_value = None):
        self.value = input_value
        self.left = None
        self.right = None

# I initialize a tree that will loook like this:
#                     1.5
#                   /     \
#           _____2.03        3.1 ___________
#          /        \          \             \
#      __ 4.05     6.03          6.2 _       6.26___
#     /     \     |     \       |      \      |      \
#   7.23    8.91  9.32   10.12  12.11  14.71  16.72   18.95 

# I initialize the nodes here.
n0 = BinaryTreeNode(1.5)
n1 = BinaryTreeNode(2.03)
n2 = BinaryTreeNode(3.1)
n3 = BinaryTreeNode(4.05)
n4 = BinaryTreeNode(6.03)
n5 = BinaryTreeNode(6.2)
n6 = BinaryTreeNode(6.26)
n7 = BinaryTreeNode(7.23)
n8 = BinaryTreeNode(8.91)
n9 = BinaryTreeNode(9.32)
n10 = BinaryTreeNode(10.12)
n11 = BinaryTreeNode(12.11)
n12 = BinaryTreeNode(14.71)
n13 = BinaryTreeNode(16.72)
n14 = BinaryTreeNode(18.95)

# I construct the tree here.
n0.left = n1
n0.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6

n3.left = n7
n3.right = n8

n4.left = n9
n4.right = n10

n5.left = n11
n5.right = n12

n6.left = n13
n6.right = n14

# Here I recursively find the sum of the binary tree
def sum_a_binary_tree(root):
    if root is None:
        return 0
    else:
        return root.value + sum_a_binary_tree(root.left) + sum_a_binary_tree(root.right)
    
results = sum_a_binary_tree(n0)

print("The sum of the provided binary tree is: ", results)

# Since there is a long trail of decimal places to this float value
# I print the results again to only two decimal places 

print("The sum of the provided binary tree is: {:.2f}".format(results))