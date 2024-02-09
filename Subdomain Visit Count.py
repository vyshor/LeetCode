class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dp = {}
        for cpdomain in cpdomains:
            (countstr, domainstr) = cpdomain.split(" ")
            count = int(countstr)
            domainsplits = domainstr.split(".")
            for i in range(len(domainsplits)):
                domain = ".".join(domainsplits[i:])
                if domain not in dp:
                    dp[domain] = count
                else:
                    dp[domain] += count

        ans = []
        for domain, count in dp.items():
            ans.append(str(count) + " " + domain)
        return ans
