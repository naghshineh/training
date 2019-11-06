class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self, val=None):
        self.root = Node(val)

    def print_tree(self, traverseType='bfs'):
        
        if (traverseType == 'bfs'):            
            return self.bfs_print(self.root)

        elif (traverseType == 'preorder'):
            return self.preorder_print(self.root, '')

        elif (traverseType == 'inorder'):
            return self.inorder_print(self.root, '')

        elif (traverseType == 'postorder'):
            return self.postorder_print(self.root, '')

    def insert(self, val):
        def _insert(start, val):
            if start:
                if (start.left == None):
                    start.left = Node(val)
                elif (start.right == None):
                    start.right = Node(val)
                elif (start.left != None):
                    _insert(start.left, val)
                elif (start.right != None):
                    _insert(start.right, val)
            else:
                if (val != None):
                    self.root = Node(val)
        _insert(self.root, val)

    # Root->Left->Right
    def preorder_print(self, start, traverse):
        if start:
            traverse += (str(start.val) + ' ')
            traverse = self.preorder_print(start.left, traverse)
            traverse = self.preorder_print(start.right, traverse)
        return traverse

    # Left->Root->Right
    def inorder_print(self, start, traverse):
        if start:
            traverse = self.preorder_print(start.left, traverse)
            traverse = self.preorder_print(start.right, traverse)
            traverse += (str(start.val) + ' ')
        return traverse

    # Left->Right->Root
    def postorder_print(self, start, traverse):
        if start:
            traverse = self.preorder_print(start.left, traverse)
            traverse += (str(start.val) + ' ')
            traverse = self.preorder_print(start.right, traverse)
        return traverse

    # Print each level from the root down
    def bfs_print(self, start):
        q = []
        q.append(start)
        result = ''
        while (len(q) > 0):
            result += str(q[0].val) + ' '
            node = q.pop(0)
            if (node.left is not None):
                q.append(node.left)
            if (node.right is not None):
                q.append(node.right)
        return result
            



            
            
tree = TreeNode(0)            
a = [1,2,3,4,5,6,7]
for x in a:
        tree.insert(x)



print(tree.print_tree('bfs'))