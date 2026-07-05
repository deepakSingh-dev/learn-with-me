from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # case 1: both empty
        if not p and not q:
            return True
        
        # case 2: one empty, one not
        if not p or not q:
            return False
        
        # case 3: values differ
        if p.val != q.val:
            return False
        
        # case 4: check subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)