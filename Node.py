
class Node:

    code = 0

    def __init__(self, name):
        self.children = []
        self.name = name
        self.code = Node.code
        Node.code += 1

    def addChild(self, node):
        self.children.append(node)
