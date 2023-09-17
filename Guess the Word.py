# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def compareWords(word1, word2):
            same = 0
            for i in range(6):
                if word1[i] == word2[i]:
                    same += 1
            return same

        dp = {}
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                dp[(words[i], words[j])] = compareWords(words[i], words[j])

        guessed_word = words[0]
        word_choices = set(words)

        while word_choices:
            correct_char = master.guess(guessed_word)
            if correct_char == 6:
                break

            word_choices.remove(guessed_word)
            new_choices = set()
            new_word = ""
            for other_word in word_choices:
                correct_count = 0
                if (guessed_word, other_word) in dp:
                    correct_count = dp[(guessed_word, other_word)]
                else:
                    correct_count = dp[(other_word, guessed_word)]

                if correct_count == correct_char:
                    if new_word == "":
                        new_word = other_word
                    new_choices.add(other_word)

            guessed_word = new_word
            word_choices = new_choices
