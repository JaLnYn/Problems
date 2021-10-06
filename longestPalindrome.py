class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s[0]
        if len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            cur_len = s[i]
            j = 1
            while i + j < len(s):
                if i - j >= 0 and s[i + j] == s[i - j]:
                    cur_len = s[i - j:i + j + 1] # do this at the end for faster
                else:
                    break
                j+=1

            if len(cur_len) > len(longest):
                longest = cur_len

            
            cur_len = s[i:i+2]
            if i + 1 < len(s) and s[i] == s[i+1]:
                j = 1
                while i + j + 1 < len(s):
                    if i - j >= 0 and s[i + j + 1] == s[i - j]:
                        cur_len = s[i-j:i+j+2]
                    else:
                        break
                    j+=1

                if len(cur_len) > len(longest):
                    longest = cur_len
        return longest

x = Solution()

print(x.longestPalindrome('cbbd'),"----assd")
print(x.longestPalindrome('babad'),"----assd")

