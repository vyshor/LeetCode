class Solution:
    def maskPII(self, s: str) -> str:

        def maskEmail(email):
            (name, domain) = email.split("@")
            return name.lower()[0] + "*" * 5 + name.lower()[-1] + "@" + domain.lower()

        def maskPhone(phone):
            sep_chars = {'+', '-', '(', ')', ' '}
            for sep_char in sep_chars:
                phone = phone.replace(sep_char, "")

            countryCode = phone[:-10]
            if countryCode:
                countryCode = "+" + "*" * len(countryCode) + "-"

            return countryCode + "***-***-" + phone[-4:]

        if "@" in s:
            return maskEmail(s)

        return maskPhone(s)
