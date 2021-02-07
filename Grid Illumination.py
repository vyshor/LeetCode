class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamp_loc = set()
        row, col, d1, d2 = {}, {}, {}, {}
        for lamp in lamps:
            lamp = tuple(lamp)
            x, y = lamp
            if x not in row.keys():
                row[x] = {lamp}
            else:
                row[x].add(lamp)

            if y not in col.keys():
                col[y] = {lamp}
            else:
                col[y].add(lamp)
            m2 = min(x, N - y - 1)
            m = min(x, y)
            x2 = x - m2
            y2 = y + m2
            x -= m
            y -= m
            if (x2, y2) not in d2.keys():
                d2[(x2,y2)] = {lamp}
            else:
                d2[(x2, y2)].add(lamp)

            if (x, y) not in d1.keys():
                d1[(x,y)] = {lamp}
            else:
                d1[(x,y)].add(lamp)
            lamp_loc.add(lamp)

        ans = []
        for query in queries:
            query = tuple(query)
            x, y = query
            m2 = min(x, N - y - 1)
            m = min(x, y)
            x2 = x - m2
            y2 = y + m2
            x3 = x - m
            y3 = y - m
            ans.append(int(len(row.get(x, ())) + len(col.get(y, ())) + len(d1.get((x3, y3), ())) + len(d2.get((x2, y2), ())) > 0))

            for i in range(-1, 2):
                for i2 in range(-1, 2):
                    if (x + i, y + i2) in lamp_loc:
                        lamp = x + i, y + i2
                        row[x + i].remove(lamp)
                        col[y + i2].remove(lamp)
                        xx, yy = x + i, y + i2
                        m2 = min(xx, N - yy - 1)
                        m = min(xx, yy)
                        x2 = xx - m2
                        y2 = yy + m2
                        x3 = xx - m
                        y3 = yy - m
                        d2[(x2, y2)].remove(lamp)
                        d1[(x3, y3)].remove(lamp)
                        lamp_loc.remove(lamp)
        return ans
# Runtime: 2272 ms, faster than 5.16% of Python3 online submissions for Grid Illumination.
# Memory Usage: 50.5 MB, less than 5.81% of Python3 online submissions for Grid Illumination.

# Time: O(N)
# Space: O(N)

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        dp = {}

        def direction_light(x, y, plus_x, plus_y, lamp):
            while 0 <= x < N and 0 <= y < N:
                if (x, y) in dp.keys():
                    dp[(x, y)].add(lamp)
                else:
                    dp[(x, y)] = {lamp}
                x += plus_x
                y += plus_y

        lamp_loc = set()
        for lamp in lamps:
            lamp = tuple(lamp)
            x, y = lamp
            lamp_loc.add(lamp)

            for i in range(-1, 2):
                for i2 in range(-1, 2):
                    if not (i == 0 and i2 == 0):
                        direction_light(x, y, i, i2, lamp)

        ans = []
        removed_light = set()
        for query in queries:
            query = tuple(query)
            x, y = query
            lit = dp.get(query)
            if not lit:
                ans.append(0)
            else:
                ans.append(int(len(lit - removed_light) > 0))

            for i in range(-1, 2):
                for i2 in range(-1, 2):
                    if (x + i, y + i2) in lamp_loc:
                        removed_light.add((x + i, y + i2))

        return ans
