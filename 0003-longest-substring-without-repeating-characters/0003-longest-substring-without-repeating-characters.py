class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub_string = ""
        max_length = 0

        for ch in s:
            if ch in sub_string:
                sub_string = sub_string[sub_string.index(ch) +1 :]

            sub_string += ch
            max_length = max(max_length, len(sub_string))

        return max_length
    

        """
        :type s: str
        :rtype: int
        """
        