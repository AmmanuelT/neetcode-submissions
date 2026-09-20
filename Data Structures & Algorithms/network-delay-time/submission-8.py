class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        res = [float('inf')] * (n + 1)
        visited = set()
        hashmap = defaultdict(list)

        for source, target, time in times:
            hashmap[source].append((time, target))

        queue = [(0,k)]

        while queue:

            time, node = heapq.heappop(queue)
            #print(f" node: {node}, time: {time}")
            visited.add(node)

            
            res[node] = min(res[node], time)

        
            
            for next_time, next_node in hashmap[node]:
                #print(f"neighbor: {neighbor}")
                if next_time + time < res[next_node]:
                    queue.append((next_time + time, next_node))
            
        
        res = res[1:]


        return max(res) if max(res) < float('inf') else -1

