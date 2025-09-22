class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pidx, tidx = 0, 0
        count = 0
        n = len(players)
        m = len(trainers)
        while pidx < n:
            while tidx < m and trainers[tidx] < players[pidx]:
                tidx += 1

            if tidx < m and players[pidx] <= trainers[tidx]:
                tidx += 1
                count += 1
            pidx += 1
        return count
