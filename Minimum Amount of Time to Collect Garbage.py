class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_pos = {'M': 0, 'P': 0, 'G':0}
        count = 0
        for i, rubbish in enumerate(garbage):
            count += len(rubbish)
            for trash in list(rubbish):
                last_pos[trash] = i

        for i, dist in enumerate(travel):
            for pos in last_pos.values():
                if pos > i:
                    count += dist

        return count
