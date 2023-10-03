class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1

        n = len(edges)
        pt1, pt2 = node1, node2
        visited1, visited2 = {node1}, {node2}

        while not (pt1 == -1 and pt2 == -1) and pt1 not in visited2 and pt2 not in visited1:

            if pt1 != -1:
                pt1 = edges[pt1]
            if pt2 != -1:
                pt2 = edges[pt2]

            if pt1 in visited1:
                pt1 = -1

            if pt2 in visited2:
                pt2 = -1

            if pt1 != -1:
                visited1.add(pt1)
            if pt2 != -1:
                visited2.add(pt2)

        ans = n
        if pt1 in visited2:
            ans = min(ans, pt1)
        if pt2 in visited1:
            ans = min(ans, pt2)

        if ans == n:
            return -1

        # print(pt1, pt2)
        # print(visited1, visited2)

        return ans
