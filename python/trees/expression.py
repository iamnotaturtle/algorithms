# Evaluation of expression tree
# https://www.geeksforgeeks.org/evaluation-of-expression-tree/
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def evaluateTree(node):
    if not node:
        return 0
    
    if not node.left and not node.right:
        return int(node.val)
    
    res = 0
    if node.val == '*':
        res = evaluateTree(node.left) * evaluateTree(node.right)
    elif node.val == '/':
        res = evaluateTree(node.left) / evaluateTree(node.right)
    elif node.val == '+':
        res = evaluateTree(node.left) + evaluateTree(node.right)
    elif node.val == '-':
        res = evaluateTree(node.left) - evaluateTree(node.right)
    
    return res

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('20')
print(evaluateTree(root))