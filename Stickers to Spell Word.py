class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counter = Counter(target)
        sticker_counter = {}

        for sticker in stickers:
            count = {}
            for c in sticker:
                if c in counter:
                    if c in count:
                        count[c] += 1
                    else:
                        count[c] = 1
            sticker_counter[sticker] = count

        visited = set()
        q = deque([(0, Counter(target))])
        while q:
            count, counter = q.popleft()
            chars = set(counter.keys())
            for sticker_count in sticker_counter.values():
                chars2 = sticker_count.keys()
                if not chars.intersection(chars2):
                    continue

                new_counter = dict(counter)
                for k, v in sticker_count.items():
                    if k in new_counter:
                        new_counter[k] -= v
                        if new_counter[k] <= 0:
                            del new_counter[k]

                if len(new_counter) == 0:
                    return count + 1
                elif str(new_counter) not in visited:
                    q.append((count + 1, new_counter))
                    visited.add(str(new_counter))

        return -1
