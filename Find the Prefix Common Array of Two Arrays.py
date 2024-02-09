class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        setA, setB = set(), set()
        common_count = 0
        ans = []
        for i in range(n):
            if A[i] in setB and A[i] not in setA:
                common_count += 1
            setA.add(A[i])

            if B[i] in setA and B[i] not in setB:
                common_count += 1
            setB.add(B[i])
            ans.append(common_count)

        return ans
