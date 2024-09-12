class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            can = True
            for c in word:
                if c not in allowed:
                    can = False
                    break
            count += int(can)
        return count
    