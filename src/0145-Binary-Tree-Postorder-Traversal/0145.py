# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ret = []
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ret.append(root.val)
            
        return self.ret


def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]
        
        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root

def printTree(root):
    if root != None:
        printTree(root.left)
        printTree(root.right) 
        print(root.val)      
            
if __name__ == "__main__":
    root = [1,None,2,3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().postorderTraversal(treeRoot))