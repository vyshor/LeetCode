class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        group_indegrees = [0] * m
        dp = {}
        group_members = {}
        group_count = {}

        for i, beforeItemArr in enumerate(beforeItems):
            for beforeItem in beforeItemArr:
                indegrees[i] += 1

                if beforeItem not in dp:
                    dp[beforeItem] = [i]
                else:
                    dp[beforeItem].append(i)

                groupIdx = group[beforeItem]
                groupIdx_i = group[i]

                if groupIdx_i != -1 and groupIdx_i != groupIdx:
                    group_indegrees[groupIdx_i] += 1

        for i, groupIdx in enumerate(group):
            if groupIdx not in group_members:
                group_members[groupIdx] = [i]
                group_count[groupIdx] = 1
            else:
                group_members[groupIdx].append(i)
                group_count[groupIdx] += 1

        groupq = deque([-1])
        itemq = deque()
        ans = []

        for groupIdx in range(m):
            if group_indegrees[groupIdx] == 0:
                groupq.append(groupIdx)

        # print(indegrees)
        # print(group_indegrees)
        # print(groupq)
        # print("==========")

        group_visited_count = -1
        while groupq:
            groupIdx = groupq.popleft()
            group_visited_count += 1

            if groupIdx not in group_members:
                continue

            for i in group_members[groupIdx]:
                if indegrees[i] == 0:
                    itemq.append(i)

            item_count = 0
            while itemq:
                i = itemq.pop()
                ans.append(i)
                # print(ans)
                if group[i] == groupIdx:
                    item_count += 1

                if i not in dp:
                    continue

                for next in dp[i]:
                    indegrees[next] -= 1

                    nextGroupIdx = group[next]
                    if nextGroupIdx != -1 and nextGroupIdx != groupIdx:
                        group_indegrees[nextGroupIdx] -= 1
                        if group_indegrees[nextGroupIdx] == 0:
                            groupq.append(nextGroupIdx)

                    if indegrees[next] == 0:
                        if group[next] == -1:
                            itemq.appendleft(next)
                        elif group[next] == groupIdx:
                            itemq.append(next)

            if groupIdx != -1 and group_count[groupIdx] > item_count:
                return []

        if m > group_visited_count:
            return []

        return ans

