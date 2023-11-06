# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map={}
        queue=[]
        queue.append(root)
        result=[]
        need = None
        while queue:
            node=queue.pop(0)
            if node.val==start:
                need=node
            if node.left:
                queue.append(node.left)
                parent_map[node.left]=node
            if node.right:
                queue.append(node.right)
                parent_map[node.right]=node      
        q=deque()
        q.append(need)
        infect=0
        
        visited=collections.defaultdict(int)
        while q:        
            # traverse left, right and parent
            levelflag=0
            q_len=len(q)
            for i in range(q_len):
                treenode=q.popleft()    
                visited[treenode]=1              
                if treenode.left and visited[treenode.left]==0:
                    visited[treenode.left]=1
                    q.append(treenode.left)
                    levelflag=1
                if treenode.right and visited[treenode.right]==0:
                    visited[treenode.right]=1
                    q.append(treenode.right)
                    levelflag=1
                #parent
                if treenode in parent_map.keys():
                    if parent_map[treenode] and visited[parent_map[treenode]]==0:
                        visited[parent_map[treenode]]=1
                        q.append(parent_map[treenode])
                        levelflag=1
            if levelflag==1:
                infect+=1
        return infect