# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Leetcode #104

class Solution:
    def recurse(self, node):
        maxDepth = 0
        if node == None:
            return maxDepth

        maxDepth += 1

        if node.left == None and node.right == None:
            return maxDepth
        else:
            maxDepth += max(self.recurse(node.left), self.recurse(node.right))
            return maxDepth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recurse(root)

solutionObject = Solution()

topNode = TreeNode(1)
secondNode1 = TreeNode(2)
secondNode2 = TreeNode(3)
thirdNode1 =  TreeNode(4)
thirdNode2 = TreeNode(5)
thirdNode4 = TreeNode(6)
thirdNode5 = TreeNode(7)

thirdNode1.left = None
thirdNode1.right = None
thirdNode2.left = None
thirdNode2.right = None
thirdNode4.left = None
thirdNode4.right = None
thirdNode5.left = None
thirdNode5.right = None

secondNode1.left = thirdNode1
secondNode1.right = thirdNode2
secondNode2.left = thirdNode4
secondNode2.right = thirdNode5

topNode.left = secondNode1
topNode.right = secondNode2

print(solutionObject.maxDepth(topNode))