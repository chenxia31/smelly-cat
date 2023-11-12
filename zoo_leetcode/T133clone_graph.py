 # Definition for a node
class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
# 每个节点的值都和它们的索引相同
# 在测试用例中用邻接列表表示图
class solution:
    def cloneGraph(self,node):
        if not node:
            return node 
        visited = {} # key: node, value: clone node

        def dfs(node):
            if node in visited:
                return visited[node]
            clone_node = Node(node.val,[])
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node
        
        return dfs(node)

# 测试用例
