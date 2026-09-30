class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        for source,target in edges:
            neighbors[source].append(target)
            neighbors[target].append(source)

        visit = set()
        def backtrack(node, prev):

            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in neighbors[node]:
                if neighbor == prev:
                    continue

                if not backtrack(neighbor, node):
                    return False
        
            return True

        res = backtrack(0,-1) and n == len(visit)
        return res
                
