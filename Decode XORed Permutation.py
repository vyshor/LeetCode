class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        full_xor = 0
        for i in range(1, n + 1):
            full_xor ^= i
        xor = 0
        for i in range(1, n - 1, 2):
            xor ^= encoded[i]
        decoded = [full_xor ^ xor]
        for num in encoded:
            decoded.append(decoded[-1] ^ num)

        return decoded
