class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        bet = (numRows - 2) * 2 + 2
        
        if numRows <= 1:
            return s

        fin = ""
        for i in range(numRows):
            j = i
            while j < len(s):
                fin = fin + s[j]
                j+= bet
                if j - i*2 < len(s) and i != 0 and i != numRows-1:
                    fin = fin + s[j-i*2]
        return fin


x= Solution()
print(x.convert('PAYPALISHIRING', 3))
print(x.convert('PAYPALISHIRING', 4))
