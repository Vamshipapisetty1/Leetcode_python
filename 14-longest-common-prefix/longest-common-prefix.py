class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)]!=prefix and prefix:
                prefix=prefix[:-1]

            if not prefix:
                return ""
        return prefix