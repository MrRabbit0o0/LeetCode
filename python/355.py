# coding: utf8

class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followed_graph = {}
        self.news_feed = {}
        self.clock = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.clock += 1
        if userId not in self.news_feed:
            self.news_feed[userId] = []
        self.news_feed[userId].append((self.clock, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self_tweet = self.news_feed.get(userId, [])[-11:]
        followee_tweet = []
        for followee_id in self.followed_graph.get(userId, set()):
            followee_tweet += self.news_feed.get(followee_id, [])[-11:]
        news_feed = self_tweet + followee_tweet
        return map(lambda x: x[1], sorted(news_feed, key=lambda x: x[0], reverse=True)[:10])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        if followerId not in self.followed_graph:
            self.followed_graph[followerId] = set()
        self.followed_graph[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        followee_set = self.followed_graph.get(followerId, set())
        followee_set.discard(followeeId)


