class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestSubstring = 0

        l, r = 0, 0
        existingChars = {}

        while r < len(s):
            if s[r] in existingChars:
                l = existingChars[s[r]] + 1
                r = l
                existingChars = {}

            existingChars[s[r]] = r
            lengthOfLongestSubstring = max(r - l + 1, lengthOfLongestSubstring)
            r += 1

        return lengthOfLongestSubstring

s = Solution()

# print("r: ", s.lengthOfLongestSubstring("bayibayi"))
print("result: ", s.lengthOfLongestSubstring("abba"))
