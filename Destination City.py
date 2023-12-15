class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for [origin, dest] in paths:
            if origin in end:
                end.remove(origin)
            else:
                start.add(origin)

            if dest in start:
                start.remove(dest)
            else:
                end.add(dest)

        return list(end)[0]
