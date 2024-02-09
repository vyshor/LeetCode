class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Each pigs is one bit
        # Each interval is one state
        # Buckets <= states^bits
        # bits >= log(states) buckets
        return math.ceil(round(math.log(buckets, (minutesToTest // minutesToDie)+1), 10))
