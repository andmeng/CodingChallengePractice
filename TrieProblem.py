
#
# A         -> A
# Single    -> Sin
# Simple    -> Sim
# Solution  -> So
#
# SolutionA -> SolutionA
# SolutionB -> SolutionB
#

class Node:

    def __init__(self, value):
        self.val = value
        self.children = {} # key: character, value: Node
        self.visited = 0 # number of times the node has been visited

class Solution:

    def getPopulatedTrie(self, strings):
        trie = Node(0)
        for str in strings:
            previousNode = trie
            for char in str:
                previousNode.visited += 1
                if (char not in previousNode.children):
                    previousNode.children[char] = Node(char)
                previousNode = previousNode.children[char]
            previousNode.visited += 1
        return trie

    def getUniquePrefixes(self, strings):
        trie = self.getPopulatedTrie(strings)
        prefixes = []
        for str in strings:
            traverse = trie
            prefix = ""

            for char in str:
                prefix += char
                traverse = traverse.children[char]
                if traverse.visited == 1:
                    prefixes.append(prefix)
                    break

        return prefixes


test = Solution()
caseOne = ["A", "Single", "Simple", "Solution"]
caseTwo = ["SolutionA", "SolutionB"]
print(test.getUniquePrefixes(caseOne))
