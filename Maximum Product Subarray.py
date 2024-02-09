class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        products = []
        j = 0
        valid_i = 0
        product = 1
        maxx = float('-inf')

        for i, num in enumerate(nums):
            if num == 0:
                maxx = max(maxx, 0)
                if i != j:
                    products.append((product, j, valid_i))
                    maxx = max(maxx, product)

                j = i + 1
                product = 1
            else:
                product *= num
                valid_i = i

        if j != n:
            products.append((product, j, valid_i))
            maxx = max(maxx, product)

        # print(products)

        for (product, i, j) in products:
            if product > 0:
                continue

            k = i
            neg_product = product
            while k < j and neg_product < 0:
                neg_product //= nums[k]
                k += 1

            if neg_product > 0:
                maxx = max(maxx, neg_product)

            k = j
            neg_product = product
            while k > i and neg_product < 0:
                neg_product //= nums[k]
                k -= 1

            if neg_product > 0:
                maxx = max(maxx, neg_product)

        return maxx
