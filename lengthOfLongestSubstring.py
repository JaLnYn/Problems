class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        
        last_seen = {}
        
        cur_index = 0

        cur_estart = 0
        for c in s:
            if c in last_seen:
                if last_seen[c] >= cur_estart:
                    # last instance of this character is 
                    if longest < cur_index - last_seen[c]:
                        longest = cur_index - last_seen[c]
                else:
                    if longest < cur_index - cur_estart + 1:
                        longest = cur_index - cur_estart + 1
                if cur_estart < last_seen[c] + 1:
                    cur_estart = last_seen[c] + 1
            else:
                if longest < cur_index - cur_estart + 1:
                    longest = cur_index - cur_estart + 1
                    #print (cur_index, cur_estart)

            last_seen[c] = cur_index
            
            cur_index += 1
        return longest 


x = Solution()


print(x.lengthOfLongestSubstring("abcabcbb"))
print(x.lengthOfLongestSubstring("bbbbb"))
print(x.lengthOfLongestSubstring("pwwkew"))
print(x.lengthOfLongestSubstring(" "))
print(x.lengthOfLongestSubstring("abba"))
print(x.lengthOfLongestSubstring("aabaab!bb"))
print(x.lengthOfLongestSubstring("aab"))


