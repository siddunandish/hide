class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

    def insert(node,data):
        if node is None:
            return(node(data))
        else:
            if data <=node.data:
                node.lef=insert(node.left,data)
            else:
                node.right=insert(node.right,data)
            return node

    def minvalue(node):
        current=Node
        while(current.left is not None):
            current=current.left
        return current.data

root=None
root=root.insert(root,4)
root.insert(root,2)
root.insert(root,5)
root.insert(root,3)
root.insert(root,6)
root.insert(root,5)
print("the minimum value of BTS ",minvalue(root))

