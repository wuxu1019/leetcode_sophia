
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class dll(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalSum(self, root):
        calc, rt = {}, []
        def verticalSumHelper(root, position):
            if not root:
                return
            if calc.has_key(position):
                calc[position] += root.val
            else:
                calc[position] = root.val
            verticalSumHelper(root.left, position-1)
            verticalSumHelper(root.right, position+1)
        verticalSumHelper(root, 0)
        for k in sorted(calc.keys()):
            rt.append(calc[k])
        return rt

    def dllverticalSum(self, root):
        if not root:
            return []
        def dllverticalSumH(root, calc):
            calc.val += root.val
            if root.left:
                if not calc.left:
                    calc.left = dll(0)
                dllverticalSumH(root.left, calc.left)
            if root.right:
                if not calc.right:
                    calc.right = dll(0)
                dllverticalSumH(root.right, calc.right)
            return calc               
     
        calc = dllverticalSumH(root, dll(0))
        rt = [calc.val] if calc.val else []
        mv = calc
        while mv.left and mv.left.val:
            rt.insert(0, mv.left.val)
            mv = mv.left
        mv = calc
        while mv.right and mv.right.val:
            rt.append(mv.right.val)
            mv = mv.right
        return rt
            
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    m = Solution()
    values = m.dllverticalSum(root)
    print values

if __name__ == '__main__':
    main()

   

