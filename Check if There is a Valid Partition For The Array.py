class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        window = deque()
        dp = set()

        eq_count = 0
        counter = {"=": 0, "<": 0, "i": 0}

        pt = 1
        while pt < n:
            if nums[pt - 1] == nums[pt]:
                window.append("=")
                counter["="] += 1
                eq_count += 1
            elif nums[pt] - nums[pt - 1] == 1:
                window.append("<")
                counter["<"] += 1
            else:
                window.append("i")
                counter["i"] += 1

            if counter["="] == 2:
                dp.add((pt - 2, pt))
            if counter["<"] == 2:
                dp.add((pt - 2, pt))
            if eq_count == 1:
                dp.add((pt - 1, pt))

            if len(window) >= 2:
                op = window.popleft()
                counter[op] -= 1

            if window[0] == "=":
                eq_count -= 1

            pt += 1

        q = [n - 1]
        visited = set()

        while q:
            i = q.pop()
            visited.add(i)
            if i - 1 >= 0 and (i - 1, i) in dp and i - 2 not in visited:
                if i - 1 == 0:
                    return True
                q.append(i - 2)
            if i - 2 >= 0 and (i - 2, i) in dp and i - 3 not in visited:
                if i - 2 == 0:
                    return True
                q.append(i - 3)
        return False

