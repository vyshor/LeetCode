class Solution:
    def sortSentence(self, s: str) -> str:
        splits = s.split(" ")
        arr = [""] * len(splits)
        for split in splits:
            pos = int(split[-1])
            arr[pos - 1] = split[:-1]
        return ' '.join(arr)
