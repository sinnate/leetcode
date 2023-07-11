# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    graph = collections.defaultdict(list)
    def calDif(self,parent,child):
         #if parent is None and child is None: return
        if child is None : return
        if parent and child :
            self.graph[child.val].append(parent.val)
            self.graph[parent.val].append(child.val)
        if child.left is None and child.right : 
           # self.calDif(child,child.left)
            self.calDif(child,child.right)
        elif child.right is None :
            self.calDif(child,child.left)
        elif child.right and child.left :
            self.calDif(child,child.left)
            self.calDif(child,child.right)
        return

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # graph = collections.defaultdict(list)
        if root.left is None and root.right is None:
            return []
        if not k:
            return [target.val]
        self.calDif(None,root)
        queue = collections.deque([target.val])
        visited = set([target])
        visited.add(target.val)
        while k :
            for i in range(len(queue)):
                parent=queue.popleft()
                visited.add(parent)
                for child in self.graph[parent] :
                    if child not in visited :
                        queue.append(child)
            k-= 1
        
        return list(queue)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        if not k:
            return [target.val]
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        result = []
        visited = set([target])

        queue = collections.deque([(target,0)])

        while queue :
            node,distance =queue.popleft()
            if distance == k :
                result.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited :
                        visited.add(edge)
                        queue.append((edge,distance + 1))
        return result


