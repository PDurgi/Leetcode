# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first do a DFS and add the parent node for each of the node in a hashmap
        parent_map={}
        queue=[]
        queue.append(root)
        result=[]
        while queue:
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
                parent_map[node.left]=node
            if node.right:
                queue.append(node.right)
                parent_map[node.right]=node      
        q=deque()
        q.append(target)
        current_distance=0
        visited=collections.defaultdict(int)
        while q:        
            # traverse left, right and parent
            q_len=len(q)
            for i in range(q_len):
                treenode=q.popleft()
                visited[treenode]=1
                if current_distance==k:
                    result.append(treenode.val)    
                if treenode.left and visited[treenode.left]==0:
                    q.append(treenode.left)
                if treenode.right and visited[treenode.right]==0:
                    q.append(treenode.right)
                #parent
                if treenode in parent_map.keys():
                    if parent_map[treenode] and visited[parent_map[treenode]]==0:
                        q.append(parent_map[treenode])
            current_distance+=1
            if current_distance>k:
                break
        return result

