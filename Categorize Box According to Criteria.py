class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        bulky, heavy = any([dist >= 10 ** 4 for dist in [length, width, height]]) or volume >= 10 ** 9, mass >= 100

        if bulky and heavy:
            return "Both"
        elif bulky and not heavy:
            return "Bulky"
        elif heavy and not bulky:
            return "Heavy"
        return "Neither"
