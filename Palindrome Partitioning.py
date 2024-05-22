class Solution:
    def partition(self, s: str) -> List[List[str]]:
        i = 0
        arr = [list(s)]
        seen = set()

        def explore(arr2):
            n = len(arr2)
            for i in range(n - 1):
                if arr2[i] == arr2[i + 1]:
                    arr3 = arr2[:i] + [arr2[i] + arr2[i + 1]] + arr2[i + 2:]
                    key = str(arr3)
                    if key not in seen:
                        seen.add(key)
                        arr.append(arr3)

            for i in range(n - 2):
                if arr2[i] == arr2[i + 2]:
                    arr3 = arr2[:i] + [arr2[i] + arr2[i + 1] + arr2[i + 2]] + arr2[i + 3:]
                    key = str(arr3)
                    if key not in seen:
                        seen.add(key)
                        arr.append(arr3)

        while i < len(arr):
            explore(arr[i])
            i += 1
        return arr
