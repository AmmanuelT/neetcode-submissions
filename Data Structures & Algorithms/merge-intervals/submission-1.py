class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 1:
            return intervals

        current_l = intervals[0][0]
        current_r = intervals[0][1]

        res = []
        for left, right in intervals[1:]:
            if left > current_r:
                res.append([current_l, current_r])
                current_l = left
                current_r = right
            elif current_l > right:
                res.append([left, right])
            else:
                current_l = min(current_l, left)
                current_r = max(current_r, right)
            #print(f'current_l: {current_l}, current_r: {current_r}')
        
        res.append([current_l, current_r])
        return res