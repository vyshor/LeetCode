class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        q = [()]

        for num, count in counter.items():
            new_q = list(q)
            for comb in q:
                for i in range(1, count + 1):
                    new_q.append(comb + ((num,) * i))
            q = new_q

        return q
