class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_TO_CHAR = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if not digits:
            return []

        
        def backtrack(i, path):
            
            if len(path) == len(digits):
                return [path]
            
            res = []
            for digit in DIGIT_TO_CHAR[digits[i]]:
                res.extend(backtrack(i+1, path + digit))
            return res
        
        return backtrack(0, "")
