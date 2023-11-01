class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = [time]
        else:
            arr = self.tweets[tweetName]
            i = bisect.bisect_left(arr, time)
            if i == len(arr):
                arr.append(time)
            else:
                arr.insert(i, time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = 86400
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600

        if tweetName not in self.tweets:
            return []

        arr = self.tweets[tweetName]
        # print(arr)

        tweetCounts = []
        for t in range(startTime, endTime+1, interval):
            i = bisect.bisect_left(arr, t)
            j = bisect.bisect_left(arr, min(t+interval, endTime+1))
            tweetCounts.append(j-i)
        return tweetCounts

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
