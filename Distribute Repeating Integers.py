class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        n = len(quantity)
        counter2 = Counter(nums)
        counter = {}

        for num, count in counter2.items():
            if count not in counter:
                counter[count] = 1
            else:
                counter[count] += 1

        quantity.sort(reverse=True)

        def giveCustomer(i):
            qty = quantity[i]
            for q in list(counter.keys()):
                if q >= qty and counter[q] > 0:
                    counter[q] -= 1
                    if counter[q] == 0:
                        del counter[q]

                    if q - qty not in counter:
                        counter[q - qty] = 1
                    else:
                        counter[q - qty] += 1

                    if i + 1 == n:
                        return True
                    else:
                        canGive = giveCustomer(i + 1)
                        if canGive:
                            return True

                    if q not in counter:
                        counter[q] = 1
                    else:
                        counter[q] += 1
                    counter[q - qty] -= 1
            return False

        return giveCustomer(0)
