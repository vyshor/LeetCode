class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n == 1:
            return True

        hand.sort()
        prev_card = hand[0]
        counter = Counter(hand)
        for i in range(groupSize):
            if prev_card + i not in counter:
                return False
            else:
                counter[prev_card + i] -= 1

        for i in range(1, n):
            startNewHand = False
            num = hand[i]
            if num != prev_card:
                if counter[prev_card] != 0:
                    return False

            if counter[num] > 0:
                for j in range(num, num+groupSize):
                    if j not in counter:
                        return False
                    else:
                        counter[j] -= 1
                        if counter[j] < 0:
                            return False

            prev_card = num

        # print(counter)
        return True
