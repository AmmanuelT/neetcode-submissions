class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_l = newInterval[0]
        new_r = newInterval[1]

        for index, (left, right) in enumerate(intervals):
            if new_l > right:
                res.append([left, right])
            elif new_r < left:
                res.append([new_l, new_r])
                res.extend(intervals[index:])
                return res
            else:
                new_l = min(new_l, left)
                new_r = max(new_r, right)
            

        res.append([new_l, new_r])
        return res