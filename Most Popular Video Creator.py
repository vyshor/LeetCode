class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        count = {}
        total_views = {}
        for i in range(n):
            creator = creators[i]
            if creator not in count:
                count[creator] = []
                total_views[creator] = 0

            video_id = ids[i]
            view = views[i]
            total_views[creator] += view
            count[creator].append((-view, video_id))

        maxx = float('-inf')
        ans = []
        for creator in count.keys():
            count[creator].sort()

            _, video_id = count[creator][0]
            max_view = total_views[creator]
            if max_view == maxx:
                ans.append([creator, video_id])
            elif max_view > maxx:
                ans = [[creator, video_id]]
                maxx = max_view

        return ans
