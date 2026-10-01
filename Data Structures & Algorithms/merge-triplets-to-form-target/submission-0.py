class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        for triplet in triplets:
            valid = True
            for i in range(3):
                if triplet[i] > target[i]:
                    valid = False
            
            if valid:
                for i in range(3):
                    res[i] = max(res[i],triplet[i])

            if res == target:
                return True
        return False