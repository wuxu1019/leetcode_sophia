"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_on(self, root):
        if not root:
            return
        queue, nextqueue = collections.deque([root]), collections.deque([])
        while queue:
            p = queue.popleft()
            if p.left:
                nextqueue.append(p.left)
            if p.right:
                nextqueue.append(p.right)
            if queue:
                p.next = queue[0]
            else:
                queue, nextqueue = nextqueue, queue

    def connect_o1(self, root):
        dummy = TreeLinkNode(0)
        point = dummy
        while root:
            while root:
                if root.left:
                    point.next = root.left
                    point = root.left
                if root.right:
                    point.next = root.right
                    point = root.right
                root = root.next
            if point == dummy:
                break
            root = dummy.next
            point = dummy

    def connect_o1(self, root):
        dummy = TreeLinkNode(0)
        point = dummy
        while root:
            point.next = root.left
            if root.left:
                point = point.next
            point.next = root.right
            if root.right:
                point = point.next
            root = root.next
            if not root:
                root = dummy.next
                point = dummy

