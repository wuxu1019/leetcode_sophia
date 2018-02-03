
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
    
def findMaxWidth(root):
    widthRecord = []
    def travesalTree(root, layer):
        if not root:
            return
        if len(widthRecord) <= layer:
            widthRecord.append(1)
        else:
            widthRecord[layer] += 1
        travesalTree(root.left, layer+1)
        travesalTree(root.right, layer+1)
    travesalTree(root, 0)
    return max(widthRecord)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
#root.right.left = TreeNode(6)
#root.right.right = TreeNode(7)
width = findMaxWidth(root)
print width

