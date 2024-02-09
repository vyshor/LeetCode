class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        prev = chars[0]
        prev_count = 1
        j = 0

        for i in range(1, n):
            if chars[i] == prev:
                prev_count += 1
            else:
                chars[j] = prev
                j += 1

                if prev_count > 1:
                    for digit in str(prev_count):
                        chars[j] = digit
                        j += 1

                prev = chars[i]
                prev_count = 1

        chars[j] = prev
        j += 1

        if prev_count > 1:
            for digit in str(prev_count):
                chars[j] = digit
                j += 1

        if len(chars) > j:
            chars.pop()

        return j
