class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.rolling_key = 0

    def getRollingKey(self):
        self.rolling_key -= 1
        return self.rolling_key

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.getRollingKey(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        followingUserIds = self.following[userId]
        followingUserIds.add(userId)
        tweets = []
        for userId in followingUserIds:
            if userId in self.tweets:
                tweets += self.tweets[userId][-10:]
        return [tweetId for (_, tweetId) in sorted(tweets)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)